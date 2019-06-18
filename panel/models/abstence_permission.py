from django.db import models
from panel.models import Customer


class AbstencePermission(models.Model):
    class Meta:
        verbose_name = 'AbstencePermission: AbstencePermission'

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    hours_absence = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'AbstencePermission #{}: {}'.format(self.id, self.name)
