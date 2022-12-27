from django import forms
from django.forms import ModelForm

from .models import Task


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ("title", "deadline", "tags")
        widgets = {
            'deadline': DateTimeInput(),
        }
