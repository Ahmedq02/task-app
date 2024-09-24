from typing import Optional
from ninja import PatchDict
from .models import Task
from .schemas import TaskIn, TaskListFilters


class TaskService:
    @staticmethod
    async def get(id: int) -> Optional[Task]:
        return await Task.objects.aget(id=id)

    @staticmethod
    async def list(filters: TaskListFilters) -> list[Task]:
        return await list(Task.objects.filter(**filters.dict()))

    @staticmethod
    async def create(schema: TaskIn) -> Task:
        return await Task.objects.acreate(**schema.dict())

    @staticmethod
    async def patch(id: int, schema: PatchDict[TaskIn]) -> Task:
        task = await Task.objects.aget(id=id)

        for key, value in schema.items():
            setattr(task, key, value)

        await task.asave()
        return task

    @staticmethod
    async def delete(id: int):
        task = await Task.objects.aget(id=id)
        await task.adelete()
