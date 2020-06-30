from django.db import models

class Resource(models.Model):

    resource_name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    thumbnail = models.URLField()
