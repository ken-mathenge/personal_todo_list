"""Create custom user forms."""
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form."""

    class Meta(UserCreationForm):
        """Meta class."""

        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """Custom user change form."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = UserChangeForm.Meta.fields
