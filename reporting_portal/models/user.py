from django.db import models
from django.contrib.auth.models import AbstractUser
from reporting_portal.constants.enums import RoleEnum

class User(AbstractUser):
    profile_pic = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(
        choices=[
            (role.value, role.name)
            for role in RoleEnum
        ]
    )

    def __str__(self):
        return self.username
