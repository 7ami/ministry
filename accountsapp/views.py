from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from operations.decorators import check_permission


from accountsapp.forms import *


def volunteer_signup(request):  # TODO: Add skill-set option after configuring server-side form
    organization = OrganizationUser.objects.all()
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            volunteerUser = form.save()
            volunteerUser.profileType = 'VolunteerUser'
            volunteerUser.save()
            auth_login(request, volunteerUser)
            return redirect('home')
    else:
        form = VolunteerSignUpForm()
    return render(request, 'signup.html', {'form': form, 'organizations': organization})


def organization_signup(request):
    organization = OrganizationUser.objects.all()
    if request.method == 'POST':
        form = OrganizationSignUpForm(request.POST, request.FILES)
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
    return render(request, 'signup.html', {'form': form, 'organizations': organization})


@login_required(login_url='login')
# @check_permission(profiletype='VolunteerUser')
def editProfile(request, username):
    organization = OrganizationUser.objects.all()
    try:
        VolunteerUser.objects.get(username=username)
    except VolunteerUser.DoesNotExist:
        try:
            OrganizationUser.objects.get(username=username)
        except OrganizationUser.DoesNotExist:
            raise Http404

        if request.method == 'POST':
            form = OrganizationUpdateForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = OrganizationUpdateForm(instance=request.user)
        return render(request, 'edit-info.html', {'form': form})

    if request.method == 'POST':
        form = VolunteerUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VolunteerUpdateForm(instance=request.user)
    return render(request, 'edit-info.html', {'form': form, 'organizations': organization})


# @login_required(login_url='login')
# @check_permission(profiletype='OrganizationUser')
# def editOrganizationInfo(request, username):
#     if request.method == 'POST':
#         form = OrganizationUpdateForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             volunteer = form.save()
#             return redirect('home')
#     else:
#         form = OrganizationUpdateForm(instance=request.user)
#     return render(request, 'edit-info.html', {'form': form})


@login_required(login_url='login')
# @check_permission(profiletype='VolunteerUser')
def viewProfile(request, username):
    organizationAll = OrganizationUser.objects.all()
    try:
        volunteer = VolunteerUser.objects.get(username=username)
    except VolunteerUser.DoesNotExist:
        try:
            organization = OrganizationUser.objects.get(username=username)
        except OrganizationUser.DoesNotExist:
            raise Http404
        return render(request, 'view-organization-profile.html', {'organizationUser': organization, 'organizations': organizationAll})
    return render(request, 'view-volunteer-profile.html', {'volunteers': volunteer, 'organizations': organizationAll})


# @login_required(login_url='login')
# @check_permission(profiletype='OrganizationUser')
# def viewOrganizations(request, username):
#     organization = get_object_or_404(OrganizationUser, username=username)
#     return render(request, 'view-organization-profile.html', {'organizations': organization})

@login_required(login_url='login')
@check_permission(profiletype='OrganizationUser')
def viewVolunteer(request,username):
    organizationall = OrganizationUser.objects.all()
    organization = get_object_or_404(OrganizationUser,username=username)
    return render(request,'organization-volunteer.html',{ 'organizations':organizationall, 'organization':organization})
