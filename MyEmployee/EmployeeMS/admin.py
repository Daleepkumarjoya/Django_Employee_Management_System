from django.contrib import admin
from .models import Employee, aboutModel


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'EmployeeId', 'PhoneNumber', 'address', 'working', 'department')
    # list_editable = ['address']
    search_fields = ['name']
    list_filter = ['working']


admin.site.register(Employee, EmployeeAdmin)


class aboutModelAdminModel(admin.ModelAdmin):
    list_display = ('AboutEMS', 'SourceName1', 'SourceAbout1', 'SourceName2', 'SourceAbout2', 'SourceName3', 'SourceAbout3')


admin.site.register(aboutModel, aboutModelAdminModel)
