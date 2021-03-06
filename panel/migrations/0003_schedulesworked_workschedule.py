# Generated by Django 2.2.2 on 2019-06-15 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_abstencepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_per_day', models.TimeField(blank=True, null=True)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('work_schedule_type', models.IntegerField(choices=[(1, 'WorkScheduleType.TYPE_HOURS'), (2, 'WorkScheduleType.TYPE_PRICE')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='panel.Customer')),
            ],
            options={
                'verbose_name': 'WorkSchedule: WorkSchedule',
            },
        ),
        migrations.CreateModel(
            name='SchedulesWorked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='panel.Customer')),
                ('work_schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='panel.WorkSchedule')),
            ],
            options={
                'verbose_name': 'SchedulesWorked: SchedulesWorked',
            },
        ),
    ]
