from django.db import models
from .resource import Resource
from .user import User

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
