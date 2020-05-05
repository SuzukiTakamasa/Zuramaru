from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """Extended User Model"""

    class Meta:
        verbose_name_plural = 'CustomUser'
