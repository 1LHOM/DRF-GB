from django.db import models
from django.contrib.auth.models import AbstractUser


class ToDoUser(AbstractUser):
    avatar = models.ImageField(blank=True, null=True)
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    birthday_year = models.SmallIntegerField(blank=True, null=True)
