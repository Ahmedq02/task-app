from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.conf import settings

class PasskeyManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(password="testpasskey")

        self.assertTrue(user.check_password("testpasskey"))
        self.assertEqual(user.username, settings.STANDARD_USER_USERNAME)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username="admin", password="testpasskey")

        self.assertTrue(admin_user.check_password("testpasskey"))
        self.assertEqual(admin_user.username, "admin")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(username="admin", password="testpasskey", is_superuser=False)