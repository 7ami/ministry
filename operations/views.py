from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import OrganizationUser, UrgencyLevel, VolunteerUser, Operation, Task
from .decorators import check_permission
from .forms import OperationCreationForm


def home(request):
    volunteer = VolunteerUser.objects.all()
    return render(request, 'home.html', {'volunteers': volunteer})


def test(request):
    volunteer = request.user
    return render(request, 'test.html', {'volunteers': volunteer})


# Trying but is of no use right now
@login_required(login_url='login')
@check_permission(profiletype='OrganizationUser')
def createOperation(request):
    if request.method == 'POST':
        form = OperationCreationForm(request.POST)
        if form.is_valid():
            operation = form.save()
            return redirect('home')
    else:
        form = OperationCreationForm()
    return render(request, 'create-operations.html', {'form': form})


# def signup(request):  # TODO: Add skill-set option after configuring server-side form
#     if request.method == 'POST':
#         form = VolunteerSignUpForm(request.POST)
#         if form.is_valid():
#             volunteer = form.save()
#             auth_login(request, volunteer)
#             return redirect('home')
#     else:
#         form = VolunteerSignUpForm()
#     return render(request, 'signup.html', {'form': form})


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