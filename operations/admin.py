from django.contrib import admin
from operations.models import UrgencyLevel, Operation, Task, Admin
from accountsapp.models import VolunteerUser, OrganizationUser


admin.site.register(VolunteerUser)
admin.site.register(OrganizationUser)
admin.site.register(UrgencyLevel)
admin.site.register(Operation, Admin)
admin.site.register(Task)
