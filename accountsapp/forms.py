from django.contrib.auth.forms import UserCreationForm
# from django import forms

from accountsapp.models import *


class VolunteerSignUpForm(UserCreationForm):

    class Meta:
        model = VolunteerUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'citizenship_Number',
                  'contact_Number', 'address', 'enrolled_Organization']


class OrganizationSignUpForm(UserCreationForm):

    class Meta:
        model = OrganizationUser
        fields = ['organization_Name', 'username', 'password1', 'password2', 'organization_ContactNo',
                  'organization_Address']
