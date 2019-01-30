from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .models import Operation, Task


class OperationCreationForm(forms.ModelForm):

    tasks = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Task.objects.all(),
        required=True
    )

    # volunteer = forms.CheckboxSelectMultiple()

    class Meta:
        model = Operation
        fields = ['operationName', 'location', 'urgencyLevel', 'volunteersRequired', 'volunteersAssigned', 'tasks',
                  'volunteer', 'organization']
