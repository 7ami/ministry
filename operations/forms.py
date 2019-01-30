from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

from .models import Operation, Task


class CustomCheckbox(Field):
    template = 'test.html'


class OperationCreationForm(forms.ModelForm):

    tasks = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Task.objects.all(),
        required=True
    )

    class Meta:
        model = Operation
        fields = ['operationName', 'location', 'volunteersRequired', 'volunteersAssigned', 'tasks']
                  # 'volunteer', 'organization']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('operationName', css_class='form-group col-md-8 mb-0'),
                # Column('urgencyLevel', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('volunteersRequired', css_class='form-group col-md-6 mb-0'),
                Column('volunteersAssigned', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            CustomCheckbox('tasks'),
            Submit('submit', 'Create')
        )
