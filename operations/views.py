from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail

from accountsapp.models import OrganizationUser,  VolunteerUser
from operations.models import Operation, Task
from operations.decorators import check_permission
from operations.forms import OperationCreationForm, OperationChangeForm, VolunteerEnrollmentForm
from django.utils.html import escapejs,mark_safe
import json



#For Urgency Leve
def scaleUrgencyLevel(Urgency):
    scale5 = Operation.objects.filter(urgencyLevel="Discretionary")
    if Urgency in scale5:
        return 5
    scale4 = Operation.objects.filter(urgencyLevel="Routine")
    if Urgency in scale4:
        return 4
    scale5 = Operation.objects.filter(urgencyLevel="High")
    if Urgency in scale5:
        return 3
    scale5 = Operation.objects.filter(urgencyLevel="Urgent")
    if Urgency in scale5:
        return 2
    scale5 = Operation.objects.filter(urgencyLevel="Emergency")
    if Urgency in scale5:
        return 1

def getUrgency(Urgency):
    if Urgency == 5:
         return 'Discretionary'
    if Urgency == 2:
         return 'Routine'
    if Urgency == 3:
        return 'High'
    if Urgency == 2:
         return 'Urgent'
    if Urgency == 1:
        return 'Emergency'



def home(request):
    volunteer = VolunteerUser.objects.all()
    operation = Operation.objects.all()
    organization = OrganizationUser.objects.all()
    locationFull = [{
        'location':[float(temp.latitude),float(temp.longitude)],
        'urgency':scaleUrgencyLevel(temp),
        'urgencyName':getUrgency(scaleUrgencyLevel(temp)),
        'volunteer':temp.volunteersAssigned,
        'quota':temp.volunteersInitial,
        'operation':temp.operationName,
        'address':temp.location

            } for temp in operation]
    context ={
        'organizations':organization,
        'volunteers':volunteer,
        'operations': operation,
        'location': mark_safe(escapejs(json.dumps(locationFull)))

    }
    return render(request, 'home.html', context= context)


# Trying but is of no use right now
@login_required(login_url='login')
@check_permission(profiletype='OrganizationUser')
def createOperation(request):
    organization = OrganizationUser.objects.all()
    if request.method == 'POST':
        form = OperationCreationForm(request.POST)
        if form.is_valid():
            operation = form.save()

            subject = 'New Relief Operation Created'

            currentUser = request.user.first_name
            currentEmail = request.user.email

            for currentOrganization in organization:
                message = currentOrganization.organization_Name + ',' + '''
                A new relief operation, ''' + operation.operationName + ' has been created in ' + operation.location + '''. Please login to the portal for further details!'''
                email_from = settings.EMAIL_HOST_USER
                recipientList = [currentOrganization.email]
                send_mail(subject, message, email_from, recipientList)

            return redirect('home')
    else:
        form = OperationCreationForm()
    return render(request, 'create-operations.html', {'form': form, 'organizations': organization})


def unauthorized(request, profileType):
    organization = OrganizationUser.objects.all()
    return render(request, 'unauthorized.html', {'profiletype': profileType, 'organizations': organization})


@login_required(login_url='login')
@check_permission(profiletype='OrganizationUser')
def changeOperation(request):
    organization = OrganizationUser.objects.all()
    if request.method == 'POST':
        form = OperationChangeForm(request.POST)
        if form.is_valid():
            currentOperation = Operation.objects.get(operationName=form.cleaned_data['operationName'])
            currentOperation.volunteersInitial = form.cleaned_data['volunteersInitial']
            currentOperation.volunteersAssigned = form.cleaned_data['volunteersAssigned']
            currentOperation.tasks.set(form.cleaned_data['tasks'])
            currentOperation.save()
            return redirect('home')
    else:
        form = OperationChangeForm()
    return render(request, 'change-operations.html', {'form': form, 'organizations': organization})


@login_required(login_url='login')
@check_permission(profiletype='OrganizationUser')
def enrollVolunteers(request):
    organization = OrganizationUser.objects.all()
    if request.method == 'POST':
        form = VolunteerEnrollmentForm(request.POST)
        if form.is_valid():
            volunteer = VolunteerUser.objects.get(username=form.cleaned_data['volunteerUsername'])
            if volunteer.enrolled_Organization == None or request.user.username == volunteer.enrolled_Organization.toString():
                operation = Operation.objects.get(operationName=form.cleaned_data['operationToEnroll'])
                operation.volunteersAssigned += 1
                operation.save()
                volunteer.operation.add(form.cleaned_data['operationToEnroll'])
                volunteer.save()

                subject = 'Assigned to a New Relief Operation'
                message = volunteer.get_full_name() + ',' + ''' You have been assigned to a new relief operation, ''' + operation.operationName + ' in ' + operation.location + '''. Please reach there and help those in need!'''
                email_from = settings.EMAIL_HOST_USER
                recipientList = [volunteer.email]
                send_mail(subject, message, email_from, recipientList)
                return redirect('home')
            else:
                return redirect('unauthorized', profileType=request.user.get_full_name())
    else:
        form = VolunteerEnrollmentForm()
    return render(request, 'enroll-volunteers.html', {'form': form, 'organizations': organization})


def viewOperations(request):
    organization = OrganizationUser.objects.all()
    operation = Operation.objects.all()
    volunteer = VolunteerUser.objects.all()
    locationFull = [{
        'location': [float(temp.latitude), float(temp.longitude)],
        'urgency': scaleUrgencyLevel(temp),
        'urgencyName': getUrgency(scaleUrgencyLevel(temp)),
        'volunteer': temp.volunteersAssigned,
        'quota': temp.volunteersInitial,
        'operation': temp.operationName,
        'address': temp.location

    } for temp in operation]
    context = {
        'organizations': organization,
        'volunteers': volunteer,
        'operations': operation,
        'location': mark_safe(escapejs(json.dumps(locationFull)))

    }
    return render(request, 'view-operations.html', context=context)
