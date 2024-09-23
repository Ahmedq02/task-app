from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class PasskeyManager(BaseUserManager):
    """
    Custom user model manager for white-listed passkeys.
    """

    def create_user(self, password, **extra_fields):
        """
        Create and return a user with an email and password.
        """
        user = self.model(username=settings.STANDARD_USER_USERNAME, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        """
        Create and return a user with superuser permissions.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
