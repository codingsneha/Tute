from django.db import models


class convert(models.Model):
    transcript = models.FileField(upload_to='documents/%Y/%m/%d')

def __str__(self):
        return self.title