from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import Passkey

class PasskeyForm(UserCreationForm):
    """
    Form for creating a new user with a passkey.
    """

    # username = forms.CharField(max_length=150, required=True, initial=settings.STANDARD_USER_USERNAME)

    class Meta:
        model = Passkey
        fields = ('password1', 'password2')