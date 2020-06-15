from django.db import models
from reporting_portal.models.user import User
from reporting_portal.models.category import Category

class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100)
    rp = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
