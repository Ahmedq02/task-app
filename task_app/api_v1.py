from ninja import NinjaAPI

api = NinjaAPI(version="0.0.0")

api.add_router("tasks", "tasks.api.router")
