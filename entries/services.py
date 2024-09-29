from typing import Optional
from asgiref.sync import sync_to_async
from ninja import PatchDict, Query
from .models import Task
from .schemas import TaskIn, TaskListFilters


class TaskService:
    @staticmethod
    async def get(id: int) -> Optional[Task]:
        return await Task.objects.aget(id=id)

    @staticmethod
    async def list(filters: TaskListFilters = Query(...)) -> list[Task]:
        tasks = await sync_to_async(Task.objects.all)()
        tasks = await sync_to_async(filters.filter)(tasks)
        return await sync_to_async(list)(tasks)

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
