from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="books",null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    publication_date = models.DateField()

    def __str__(self):
        return self.title