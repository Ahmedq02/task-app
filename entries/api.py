from ninja import Router, PatchDict, Query
from ninja.pagination import paginate
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user

from entries.models import Task
from .services import TaskService
from .schemas import TaskIn, TaskListFilters, TaskOut


async def async_auth(request):
    user = await sync_to_async(get_user)(request)
    if user.is_authenticated:
        return user
    return None


router = Router(auth=async_auth)


@router.get("/", response=list[TaskOut])
@paginate(limit=10, offset=0)
async def list_tasks(request, filters: TaskListFilters = Query(...)):
    return await TaskService.list(filters)


@router.get("/{task_id}", response={200: TaskOut, 404: None})
async def get_task(request, task_id: int):
    try:
        return await TaskService.get(task_id)
    except Task.DoesNotExist:
        return 404


@router.post("/", response=TaskOut)
async def create_task(request, payload: TaskIn):
    return await TaskService.create(payload)


@router.put("/{task_id}", response={200: TaskOut, 404: None})
async def update_task(request, task_id: int, payload: PatchDict[TaskIn]):
    try:
        return await TaskService.patch(task_id, payload)
    except Task.DoesNotExist:
        return 404


@router.delete("/{task_id}", response={204: None, 404: None})
async def delete_task(request, task_id: int):
    try:
        await TaskService.delete(task_id)
        return 204
    except Task.DoesNotExist:
        return 404
