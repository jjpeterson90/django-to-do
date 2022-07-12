from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AppUser(AbstractUser):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 55,
        unique = True,
    )
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now, editable=False)
