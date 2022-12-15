""" from django.db import models
from django.contrib.auth.models import User


class convert(models.Model):
    transcript = models.FileField(upload_to='documents/%Y/%m/%d')

def __str__(self):
        return self.title """