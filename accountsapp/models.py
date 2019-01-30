from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):

    profileType = models.CharField(max_length=300)

    def __str__(self):
        if self.profileType == 'AdminUser':
            return self.username

        else:
            return self.get_full_name()


# This is not used right now but if we make our own admin page, this might be useful
class AdminUser(BaseUser):

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def save(self, *args, **kwargs):
        self.profileType = 'AdminUser'
        super().save(*args, **kwargs)


class OrganizationUser(BaseUser):

    organization_Name = models.CharField(max_length=30, unique=True, verbose_name='Organization Name')
    organization_ContactNo = models.BigIntegerField(verbose_name='Contact Number')
    organization_Address = models.CharField(max_length=255, verbose_name='Address')
    is_staff = True

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def save(self, *args, **kwargs):
        self.profileType = 'OrganizationUser'
        self.first_name = self.organization_Name
        self.last_name = ''
        super().save(*args, **kwargs)


class VolunteerUser(BaseUser):

    citizenship_Number = models.BigIntegerField(verbose_name='Citizenship Number', unique=True)
    contact_Number = models.BigIntegerField(verbose_name='Contact Number')
    address = models.CharField(max_length=255)
    enrolled_Organization = models.ForeignKey(OrganizationUser, on_delete=models.CASCADE, to_field='organization_Name',
                                              related_name='volunteers', null=True, blank=True)

    class Meta:
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'

    def save(self, *args, **kwargs):
            self.profileType = 'VolunteerUser'
            super().save(*args, **kwargs)
