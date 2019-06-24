# Generated by Django 2.2.2 on 2019-06-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_schedulesworked_workschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workschedule',
            name='price_per_day',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]