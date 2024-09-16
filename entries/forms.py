from django.forms import ModelForm
from entries.models import Task
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    due_by = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local"})
    )

    priority = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
