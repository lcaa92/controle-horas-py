from django.contrib import admin
from panel.models import Customer, AbstencePermission, WorkSchedule, SchedulesWorked
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class AbstencePermissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(AbstencePermission, AbstencePermissionAdmin)

class WorkScheduleAdmin(admin.ModelAdmin):
    pass
admin.site.register(WorkSchedule, WorkScheduleAdmin)

class SchedulesWorkedAdmin(admin.ModelAdmin):
    pass
admin.site.register(SchedulesWorked, SchedulesWorkedAdmin)
