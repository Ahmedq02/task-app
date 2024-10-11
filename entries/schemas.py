from ninja import ModelSchema, FilterSchema, Field
from typing import Optional
from django.utils.timezone import datetime
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
    due_by__gte: Optional[datetime] = Field(None, alias="start", ignore_none=True)
    due_by__lte: Optional[datetime] = Field(None, alias="end", ignore_none=True)
    priority: Optional[int] = Field(None, ignore_none=True)
