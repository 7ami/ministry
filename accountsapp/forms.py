from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django import forms

from accountsapp.models import *


class VolunteerSignUpForm(UserCreationForm):

    class Meta:
        model = VolunteerUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'citizenship_Number',
                  'contact_Number', 'address', 'enrolled_Organization', 'profilePicture']


class OrganizationSignUpForm(UserCreationForm):

    class Meta:
        model = OrganizationUser
        fields = ['organization_Name', 'username', 'password1', 'password2', 'email', 'organization_ContactNo',
                  'organization_Address', 'profilePicture']


class VolunteerUpdateForm(UserChangeForm):

    class Meta:
        model = VolunteerUser
        fields = ['first_name', 'last_name', 'username', 'email', 'citizenship_Number', 'contact_Number',
                  'address', 'enrolled_Organization', 'profilePicture']


class OrganizationUpdateForm(UserChangeForm):

    class Meta:
        model = OrganizationUser
        fields = ['organization_Name', 'username', 'organization_ContactNo', 'organization_Address', 'profilePicture']
