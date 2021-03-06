from django.core.management.base import BaseCommand
from django.db import connections, transaction
from panel.models import Customer, WorkSchedule, SchedulesWorked, AbstencePermission
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Import data from MySQL Database'

    USER_MIGRATE = User.objects.get(id=1)

    arr_migration_customer = {}
    arr_migration_workscheduler = {}

    def import_customers(self, conn):
        self.stdout.write(self.style.WARNING('Import customers'))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()

        for customer_data in customers:
            (id, customer_type, customer_document, name, email, phone,  user_id, created_at, updated_at, deleted_at,
             contract_type) = customer_data
            customer, created_now = Customer.objects.get_or_create(
                name=name,
                active=True if not deleted_at else False,
                user=self.USER_MIGRATE,
                customer_type=customer_type,
                customer_document=customer_document,
                email=email,
                phone=phone,
                contract_type=contract_type,
            )

            if created_now:
                customer.created_at = created_at
                customer.deleted_at = deleted_at
                customer.save()
                print('Customer {name} has been import'.format(name=customer.name))
            else:
                print('Customer {name} already imported'.format(name=customer.name))

            self.arr_migration_customer.update({id: customer})

    def import_workschedule(self, conn):
        self.stdout.write(self.style.WARNING('Importing Work Schedules'))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM work_schedule")
            work_schedules = cursor.fetchall()

        for ws in work_schedules:
            (id, ws_type, description, hours_per_dar, price_per_day, created_at, updated_at, deleted_at, user_id,
             customer_id) = ws

            work_schedule, created_now = WorkSchedule.objects.get_or_create(
                customer_id=self.arr_migration_customer[customer_id].id,
                hours_per_day=hours_per_dar,
                price_per_day=price_per_day,
                description=description,
                work_schedule_type=WorkSchedule.WorkScheduleType(ws_type).value
            )

            if created_now:
                work_schedule.created_at = created_at
                work_schedule.deleted = deleted_at
                work_schedule.save()
                print('WorkSchedule {description} has been import'.format(description=work_schedule.description))
            else:
                print('WorkSchedule {description} already imported'.format(description=work_schedule.description))

            self.arr_migration_workscheduler.update({id: work_schedule})

    def import_schedulesworked(self, conn):
        self.stdout.write(self.style.WARNING('Importing Schedules Worked'))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM schedules_worked")
            schedules_worked = cursor.fetchall()

        for sw in schedules_worked:
            (id, user_id, customer_id, start_time, end_time, created_at, updated_at, deleted_at, work_schedule_id) = sw

            scheduleworked, created_now = SchedulesWorked.objects.get_or_create(
                customer_id=self.arr_migration_customer[customer_id].id,
                start_time=start_time,
                end_time=end_time,
                work_schedule_id=self.arr_migration_workscheduler[work_schedule_id],
            )

            if created_now:
                scheduleworked.created_at = created_at
                scheduleworked.deleted = deleted_at
                scheduleworked.save()
                print('ScheduleWork {start} - {end} has been import'.format(start=start_time, end=end_time))
            else:
                print('ScheduleWork {start} - {end} already imported'.format(start=start_time, end=end_time))

    def import_abstencepermission(self, conn):
        self.stdout.write(self.style.WARNING('Importing Abstence Permission'))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM absence_permission")
            abstence_permission = cursor.fetchall()

        for ap in abstence_permission:
            (id, user_id, customer_id, date, hours_absence, description, created_at, updated_at, deleted_at) = ap
            abstence, created_now = AbstencePermission.objects.get_or_create(
                customer_id=self.arr_migration_customer[customer_id].id,
                description=description,
                date=date,
                hours_absence=hours_absence,
            )

            if created_now:
                abstence.created_at = created_at
                abstence.deleted = deleted_at
                abstence.save()
                print('Abstence {description} has been import'.format(description=description))
            else:
                print('Abstence {description} already imported'.format(description=description))

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Import mysql data'))

        mysql_conn = connections['mysql']

        with transaction.atomic():
            self.import_customers(mysql_conn)
            self.import_workschedule(mysql_conn)
            self.import_schedulesworked(mysql_conn)
            self.import_abstencepermission(mysql_conn)
