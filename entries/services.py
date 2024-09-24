from typing import Optional
from .models import Task
from .schemas import TaskIn
from django.core.exceptions import ObjectDoesNotExist


class TaskService:
    def get(self, id: int) -> Optional[Task]:
        return Task.objects.get(id=id)

    def list(self, filters):
        pass

    def create(self, schema: TaskIn) -> Task:
        return Task.objects.acreate(**schema.dict())

    def patch(self, id: int, schema: TaskIn) -> Task:
        task = self.get(id=id)
        if not task:
            raise ObjectDoesNotExist("Task does not exist")

        for key, value in schema.dict().items():
            setattr(task, key, value)

        task.save()
        return task

    def delete(self, id: int):
        task = self.get(id=id)
        task.delete()
