from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import os


class Command(BaseCommand):
    help = "Crete passkey from environment variables"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Get the passkey of standard user from environment variables
        password = os.getenv("PASSKEY")
        username = os.getenv("STANDARD_USER_USERNAME")

        # Create standard user
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(password=password)
            self.stdout.write(self.style.SUCCESS("Passkey created successfully"))

        else:
            self.stdout.write(self.style.SUCCESS("Passkey already exists"))
