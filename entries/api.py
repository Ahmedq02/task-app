from ninja import Router

router = Router()


@router.get("/")
def list_tasks(request):
    pass


@router.get("/{task_id}")
def get_task(request, task_id: int):
    pass


@router.post("/")
def create_task(request):
    pass


@router.put("/{task_id}")
def update_task(request, task_id: int):
    pass


@router.delete("/{task_id}")
def delete_task(request, task_id: int):
    pass
