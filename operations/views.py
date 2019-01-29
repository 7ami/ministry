from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .models import Organization, UrgencyLevel, Volunteer, VolunteerAssigned, VolunteerRequired, Operation, Task

from .forms import VolunteerSignUpForm, LoginForm


def home(request):
    volunteer = Volunteer.objects.all()
    return render(request, 'home.html', {'volunteers': volunteer})


def test(request):
    volunteer = request.user
    return render(request, 'test.html', {'volunteers': volunteer})


def signup(request):  # TODO: Add skill-set option after configuring server-side form
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST)
        if form.is_valid():
            volunteer = form.save()
            auth_login(request, volunteer)
            return redirect('home')
    else:
        form = VolunteerSignUpForm()
    return render(request, 'signup.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             volunteer = form.save()
#             auth_login(request, volunteer)
#             return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})