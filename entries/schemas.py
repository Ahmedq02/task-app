from ninja import ModelSchema
from .models import Task


class TaskIn(ModelSchema):
    class Meta:
        model = Task
        except_ = ["id"]


class TaskOut(ModelSchema):
    class Meta:
        model = Task
        fields = "__all__"
