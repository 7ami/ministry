from django.contrib import admin
from .models import VolunteerUser, OrganizationUser, UrgencyLevel, Operation, Task, Admin


admin.site.register(VolunteerUser)
admin.site.register(OrganizationUser)
admin.site.register(UrgencyLevel)
admin.site.register(Operation, Admin)
admin.site.register(Task)
