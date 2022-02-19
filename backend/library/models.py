from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=64, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.IntegerField()
    email = models.EmailField(max_length=254, unique=True, null=True)
