from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from operations.models import Operation


class BaseUser(AbstractUser):

    profileType = models.CharField(max_length=300)

    def __str__(self):
        if self.profileType == 'AdminUser':
            return self.username

        else:
            return self.username

    def toString(self):
        return self.username


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
    profilePicture = models.ImageField(
        upload_to='organizations/',
        verbose_name='Profile Picture',
        default='default.jpg'
    )
    is_staff = True
    operation = models.ManyToManyField(Operation, related_name='organizations', blank=True)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def save(self, *args, **kwargs):
        self.profileType = 'OrganizationUser'
        self.first_name = self.organization_Name
        self.last_name = ''
        super().save(*args, **kwargs)

        img = Image.open(self.profilePicture.path)
        if img.height > 300 or img.width > 300:
            outputSize = (300, 300)
            img.thumbnail(outputSize)
            img.save(self.profilePicture.path)


class VolunteerUser(BaseUser):

    citizenship_Number = models.BigIntegerField(verbose_name='Citizenship Number', unique=True)
    contact_Number = models.BigIntegerField(verbose_name='Contact Number')
    address = models.CharField(max_length=255)
    enrolled_Organization = models.ForeignKey(OrganizationUser, on_delete=models.CASCADE, to_field='organization_Name',
                                              related_name='volunteers', null=True, blank=True)
    operation = models.ManyToManyField(Operation, related_name='volunteers', blank=True)
    profilePicture = models.ImageField(
        upload_to='volunteers/',
        verbose_name='Profile Picture',
        default='default.jpg'
    )

    class Meta:
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'

    def save(self, *args, **kwargs):
            self.profileType = 'VolunteerUser'
            super().save(*args, **kwargs)

            # if self.profilePicture.path

            img = Image.open(self.profilePicture.path)
            if img.height > 300 or img.width > 300:
                outputSize = (300, 300)
                img.thumbnail(outputSize)
                img.save(self.profilePicture.path)
