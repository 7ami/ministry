from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

from operations.models import Operation, Task
from accountsapp.models import VolunteerUser


# class CustomCheckbox(Field):
#     template = 'test.html'


class OperationCreationForm(forms.ModelForm):

    tasks = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Task.objects.all(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Row(
            Column('operationName', css_class='form-group col-md-12 mb-0'),
            Column('location', css_class='form-group col-md-12 mb-0'),
            Column('urgencyLevel', css_class='form-group col-md-6 mb-0'),
                # css_class='form-row'
            # ),
            # Row(
            Column('volunteersInitial', css_class='form-group col-md-6 mb-0'),
            Column('volunteersAssigned', css_class='form-group col-md-6 mb-0'),
                # css_class='form-row'
            # ),
            Column('tasks', css_class='form-group, col-md-6 mb-3'),

            Submit(type='submit', value='Create', name='Create', css_class='ml-3 form-group btn-primary btn-primary-success')
        )

    class Meta:
        model = Operation
        fields = ['operationName', 'location', 'urgencyLevel', 'volunteersInitial', 'volunteersAssigned', 'tasks','latitude','longitude']
                  # 'volunteer', 'organization']


class OperationChangeForm(forms.Form):

    operationName = forms.ModelChoiceField(queryset=Operation.objects.all(), label='Operation Name')
    volunteersInitial = forms.IntegerField(label='Estimated Number of Required Volunteers')
    volunteersAssigned = forms.IntegerField(label='Total Volunteers in the area')

    tasks = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Task.objects.all(),
        required=True
    )


class VolunteerEnrollmentForm(forms.Form):

    volunteerUsername = forms.ModelChoiceField(queryset=VolunteerUser.objects.all(),
                                               label='Volunteer Username')
    operationToEnroll = forms.ModelChoiceField(queryset=Operation.objects.all(), label='Operation to Enroll to')
    task = forms.ModelChoiceField(queryset=Task.objects.all(), widget=forms.RadioSelect(), label='Involve in')
