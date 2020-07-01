from django.db import models
from .resource import Resource
from resource_management.constants.enums import AccessLevelEnum

class Item(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class UserItems(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    access_level = models.CharField(
        choices=[
            (access.value, access.name)
            for access in AccessLevelEnum
        ],
        max_length=100, default=AccessLevelEnum.READ.value
    )
    user_id = models.IntegerField()
