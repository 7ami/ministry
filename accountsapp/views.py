from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from accountsapp.forms import *


def volunteer_signup(request):  # TODO: Add skill-set option after configuring server-side form
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST)
        if form.is_valid():
            volunteerUser = form.save()
            volunteerUser.profileType = 'VolunteerUser'
            volunteerUser.save()
            auth_login(request, volunteerUser)
            return redirect('home')
    else:
        form = VolunteerSignUpForm()
    return render(request, 'signup.html', {'form': form})

def organization_signup(request):
    if request.method == 'POST':
        form = OrganizationSignUpForm(request.POST)
        if form.is_valid():
            organizationUser = form.save()
            organizationUser.profileType = 'OrganizationUser'
            organizationUser.save()
            auth_login(request, organizationUser)
            print(form.cleaned_data['username'])
            print(form.cleaned_data['organization_Name'])
            print(form.cleaned_data['organization_ContactNo'])
            print(form.cleaned_data['organization_Address'])
            return redirect('home')
    else:
        form = OrganizationSignUpForm()
    return render(request, 'signup.html', {'form': form})
