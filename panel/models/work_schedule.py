from enum import Enum
from django.db import models
from panel.models import Customer


class WorkSchedule(models.Model):
    class Meta:
        verbose_name = 'WorkSchedule: WorkSchedule'

    class WorkScheduleType(Enum):
        def as_tuple(self):
            return self.value, str(self)

        @classmethod
        def choices(cls):
            return[x.as_tuple() for x in list(cls)]

        TYPE_HOURS = 1
        TYPE_PRICE = 2

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    hours_per_day = models.TimeField(null=True, blank=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    work_schedule_type = models.IntegerField(choices=WorkScheduleType.choices())
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'WorkSchedule #{}: {}'.format(self.id, self.description)
