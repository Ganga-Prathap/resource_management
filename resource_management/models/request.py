from django.db import models
from .user import User
from .item import Item
from resource_management.constants.enums import (
    AccessLevelEnum,
    StatusLevelEnum
)

class Request(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
