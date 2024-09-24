from ninja import ModelSchema, FilterSchema, Field
from typing import Optional
from django.utils.timezone import datetime, timedelta
from .models import Task


class TaskIn(ModelSchema):
    class Meta:
        model = Task
        exclude = ["id"]


class TaskOut(ModelSchema):
    class Meta:
        model = Task
        fields = "__all__"


class TaskListFilters(FilterSchema):
    start: Optional[datetime] = Field(datetime.now(), q="due_by__gte")
    end: Optional[datetime] = Field(
        datetime.now() + timedelta(days=30), q="due_by__lte"
    )
    priority: Optional[int]
