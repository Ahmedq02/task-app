from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.conf import settings

class PasskeyBackend(BaseBackend):
    """
    Custom authentication backend for white-listed passkeys.
    """
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        if username is None:
            username = settings.STANDARD_USER_USERNAME
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None