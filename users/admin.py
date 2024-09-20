from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import PasskeyForm
from .models import Passkey

class PasskeyAdmin(UserAdmin):
    add_form = PasskeyForm
    model = Passkey
    list_display = ['username', 'is_staff', 'is_active']
    list_filter = ['username', 'is_staff', 'is_active']

    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ['username']
    ordering = ['username']

admin.site.register(Passkey, PasskeyAdmin)