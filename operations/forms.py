from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


from .models import Volunteer


class VolunteerSignUpForm(UserCreationForm):

    citizenship_Number = forms.CharField(
        widget=forms.TextInput(),
        max_length=15
    )

    contact_Number = forms.IntegerField(
        widget=forms.NumberInput()
    )

    address = forms.CharField(
        widget=forms.TextInput(),
        max_length=255
    )

    email = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.EmailInput()
    )

    enrolled_Organization = forms.CharField(
        widget=forms.TextInput(),
        max_length=255
    )

    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'citizenship_Number',
                  'contact_Number', 'address', 'enrolled_Organization']


class LoginForm(UserCreationForm):

    class Meta:
        model = Volunteer
        fields = ['username']