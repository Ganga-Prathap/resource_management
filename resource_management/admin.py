from django.contrib import admin
from resource_management.models.user import User
from resource_management.models.resource import Resource
from resource_management.models.item import Item
from resource_management.models.request import Request

admin.site.register(User)
admin.site.register(Resource)
admin.site.register(Item)
admin.site.register(Request)
