from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    publication_date = models.DateField()

    def __str__(self):
        return self.title