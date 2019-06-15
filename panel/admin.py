from django.contrib import admin
from panel.models import Customer, AbstencePermission
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)


class AbstencePermissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(AbstencePermission, AbstencePermissionAdmin)
