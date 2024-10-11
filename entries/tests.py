from django.test import TestCase
from django.utils import timezone
from .models import Task
from .services import TaskService
from .schemas import TaskIn
from ninja import PatchDict


class TaskServiceTest(TestCase):
    async def test_create_task(self):
        task_in = TaskIn(
            user_email="test@test.com",
            task="Test Task",
            due_by=timezone.now(),
            priority=1,
            is_urgent=False,
        )

        task = await TaskService.create(task_in)

        self.assertEqual(task.user_email, task_in.user_email)
        self.assertEqual(task.task, task_in.task)
        self.assertEqual(task.due_by, task_in.due_by)
        self.assertEqual(task.priority, task_in.priority)
        self.assertEqual(task.is_urgent, task_in.is_urgent)
        self.assertIsNotNone(task.id)

    async def test_delete_task(self):
        task_in = TaskIn(
            user_email="test@test.com",
            task="Test Task",
            due_by=timezone.now(),
            priority=1,
            is_urgent=False,
        )

        task = await TaskService.create(task_in)
        task_id = task.id

        await TaskService.delete(task_id)

        with self.assertRaises(Task.DoesNotExist):
            await TaskService.get(task_id)

    async def test_patch_task(self):
        task_in = TaskIn(
            user_email="test@test.com",
            task="Test Task",
            due_by=timezone.now(),
            priority=1,
            is_urgent=False,
        )

        task = await TaskService.create(task_in)

        patch_dict = PatchDict[TaskIn](
            user_email="test2@test.com",
        )

        task = await TaskService.patch(task.id, patch_dict)

        self.assertEqual(task.user_email, "test2@test.com")

    async def test_get_task(self):
        task_in = TaskIn(
            user_email="test@test.com",
            task="Test Task",
            due_by=timezone.now(),
            priority=1,
            is_urgent=False,
        )

        task = await TaskService.create(task_in)

        task = await TaskService.get(task.id)

        self.assertEqual(task.user_email, task_in.user_email)
        self.assertEqual(task.task, task_in.task)
        self.assertEqual(task.due_by, task_in.due_by)
        self.assertEqual(task.priority, task_in.priority)
        self.assertEqual(task.is_urgent, task_in.is_urgent)
        self.assertIsNotNone(task.id)
