from django.db import models
from panel.models import Customer, WorkSchedule


class SchedulesWorked(models.Model):
    class Meta:
        verbose_name = 'SchedulesWorked: SchedulesWorked'

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    work_schedule_id = models.ForeignKey(WorkSchedule, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'SchedulesWorked #{}: {} - {}'.format(self.id, self.start_time, self.end_time)
