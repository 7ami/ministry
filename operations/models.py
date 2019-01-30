from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

from accountsapp.models import *


class UrgencyLevel(models.Model):
    urgency = models.CharField(max_length=50, unique=True)
    urgencyScale = models.IntegerField()

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
    volunteersInitial = models.IntegerField(verbose_name='Estimated Number of Required Volunteers')

    volunteersRequired = models.IntegerField(verbose_name='Currently Required Number', default=0)

    volunteer = models.ManyToManyField(VolunteerUser, related_name='operations', blank=True)
    tasks = models.ManyToManyField(Task, related_name='+')
    organization = models.ManyToManyField(OrganizationUser, related_name='operations', blank=True)

    def __str__(self):
        return self.operationName

    def save(self, *args, **kwargs):

        self. volunteersRequired = self.volunteersInitial - self.volunteersAssigned
        for count in range(1, UrgencyLevel.objects.all().count()+1):

            if (self.volunteersAssigned/self.volunteersInitial) <= count*(1/UrgencyLevel.objects.all().count()):
                self.urgencyLevel = UrgencyLevel.objects.get(urgencyScale=count)
                break

        super().save(*args, **kwargs)



class Admin(admin.ModelAdmin):

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }