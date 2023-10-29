from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class target(models.Model):
    title = models.CharField(max_length=20)
    Desc = models.TextField()
    time = models.DateField()
    status = models.CharField(max_length=6)   