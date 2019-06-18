from django.core.management.base import BaseCommand, CommandError
from django.db import connections, transaction
from panel.models import Customer, WorkSchedule, SchedulesWorked, AbstencePermission

class Command(BaseCommand):
    help = 'Import data from MySQL Database'
    
    def import_customers(self, conn):
        self.stdout.write(self.style.WARNING('Import customers'))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()

        for customer in customers:
            (id, customer_type, customer_document, name, email, phone,  user_id, created_at, updated_at, deleted_at, contract_type) = customer
            print(customer)

    def import_workschedule(self, conn):
        self.stdout.write(self.style.WARNING('Importing Work Schedules'))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM work_schedule")
            work_schedules = cursor.fetchall()

        for ws in work_schedules:
            (id, ws_type, description, hours_per_dar, price_per_day, created_at, updated_at, deleted_at, user_id, customer_id) = ws
            print(ws)

    def import_schedulesworked(self, conn):
        self.stdout.write(self.style.WARNING('Importing Schedules Worked'))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM schedules_worked")
            schedules_worked = cursor.fetchall()

        for sw in schedules_worked:
            (id, user_id, customer_id, start_time, end_time, created_at, updated_at, deleted_at, work_schedule_id) = sw
            print(sw)

    def import_abstencepermission(self, conn):
        self.stdout.write(self.style.WARNING('Importing Abstence Permission'))

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM absence_permission")
            absence_permission = cursor.fetchall()

        for ap in absence_permission:
            (id, user_id, customer_id, date, hours_absence, description, created_at, updated_at, deleted_at) = ap
            print(ap)

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Import mysql data'))

        mysql_conn = connections['mysql']

        with transaction.atomic():
            self.import_customers(mysql_conn)
            self.import_workschedule(mysql_conn)
            self.import_schedulesworked(mysql_conn)
            self.import_abstencepermission(mysql_conn)
