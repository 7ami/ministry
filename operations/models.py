from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

from accountsapp.models import *


class UrgencyLevel(models.Model):
    urgency = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.urgency


# class VolunteerRequired(models.Model):
#     requiredNumber = models.IntegerField()
#
#
# class VolunteerAssigned(models.Model):
#     assignedNumber = models.IntegerField()


class Task(models.Model):
    task = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.task


class Operation(models.Model):

    operationName = models.CharField(max_length=30, unique=True, verbose_name='Operation Name')
    location = models.CharField(max_length=255, unique=True)
    urgencyLevel = models.ForeignKey(UrgencyLevel, on_delete=models.CASCADE, related_name='+',
                                     verbose_name='Urgency Level')
    volunteersAssigned = models.IntegerField(verbose_name='Total Volunteers in the area', default=0)
    volunteersRequired = models.IntegerField(verbose_name='Estimated number of required volunteers')
    volunteer = models.ManyToManyField(VolunteerUser, related_name='operations')
    tasks = models.ManyToManyField(Task, related_name='+')
    organization = models.ManyToManyField(OrganizationUser, related_name='operations')

    def __str__(self):
        return self.operationName


class Admin(admin.ModelAdmin):

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }