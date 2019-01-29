from django.db import models
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    organizationName = models.CharField(max_length=30, unique=True)
    organizationContactNo = models.BigIntegerField()
    organizationAddress = models.CharField(max_length=255)


class UrgencyLevel(models.Model):
    urgency = models.CharField(max_length=50, unique=True)


class VolunteerRequired(models.Model):
    requiredNumber = models.IntegerField()


class VolunteerAssigned(models.Model):
    assignedNumber = models.IntegerField()


class Task(models.Model):
    task = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)


class Volunteer(AbstractUser):
    citizenship_Number = models.BigIntegerField()
    contact_Number = models.BigIntegerField()
    address = models.CharField(max_length=255)
    # enrolled_Organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='volunteers', blank=True)


class Operation(models.Model):
    operationName = models.CharField(max_length=30, unique=True)
    location = models.CharField(max_length=255, unique=True)
    urgencyLevel = models.ForeignKey(UrgencyLevel, on_delete=models.CASCADE, related_name='+')
    volunteersAssigned = models.OneToOneField(VolunteerAssigned, on_delete=models.CASCADE, related_name='operations')
    volunteersRequired = models.OneToOneField(VolunteerRequired, on_delete=models.CASCADE, related_name='operations')
    volunteer = models.ManyToManyField(Volunteer, related_name='operations')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='+')
    organization = models.ManyToManyField(Organization, related_name='operations')
