from django.forms import ModelForm
from entries.models import Task
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    due_by = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local"})
    )
