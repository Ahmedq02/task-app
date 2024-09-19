from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .managers import PasskeyManager

class Passkey(AbstractUser):
    """
    Custom user model for white-listed passkeys.
    """
    objects = PasskeyManager()