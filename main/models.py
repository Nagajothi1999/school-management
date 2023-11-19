from django.db import models
from django.contrib.auth.models import AbstractUser
from .constant import ROLE_CHOICES


# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    country = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_user_groups',  # Adjusted related name
        related_query_name='main_user_group',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_user_user_permissions',  # Adjusted related name
        related_query_name='main_user_user_permission',
    )