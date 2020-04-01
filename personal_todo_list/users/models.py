"""User models."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model."""

    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        """Return email in human readable form."""
        return self.email
