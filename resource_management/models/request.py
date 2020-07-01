from django.db import models
from .item import Item
from resource_management.constants.enums import (
    AccessLevelEnum,
    StatusLevelEnum
)

class Request(models.Model):

    user_id = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    access_level = models.CharField(
        choices=[
            (access.value, access.name)
            for access in AccessLevelEnum
        ],
        max_length=100
    )

    due_date_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField()

    status = models.CharField(
        choices=[
            (status.value, status.name)
            for status in StatusLevelEnum
        ],
        max_length=100, default=StatusLevelEnum.PENDING.value
    )
