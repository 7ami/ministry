from django.contrib import admin
from operations.models import UrgencyLevel, Operation, Task, Admin
from accountsapp.models import VolunteerUser, OrganizationUser
from import_export.admin import ImportExportModelAdmin

admin.site.register(Operation, Admin)
@admin.register(UrgencyLevel, Task)
@admin.register(VolunteerUser, OrganizationUser)
class ViewAdmin(ImportExportModelAdmin):
    pass
