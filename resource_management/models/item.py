from django.db import models
from .resource import Resource


class Item(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class UserItems(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.IntegerField()
