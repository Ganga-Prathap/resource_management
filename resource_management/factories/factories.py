import factory
from resource_management.models.resource import Resource
from resource_management.models.item import Item, UserItems
from resource_management.models.request import Request
from resource_management.constants.enums import (
    AccessLevelEnum,
    StatusLevelEnum
)


ACCESS_LEVEL_CHOICES=[
        access.value
        for access in AccessLevelEnum
    ]

class ResourceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Resource

    resource_name = factory.Sequence(lambda n: "resource_name-%d" % n)
    description = factory.Sequence(lambda n: "description-%d" % n)
    link = factory.Sequence(lambda n: "https://link-%d" % n)
    thumbnail = factory.Sequence(lambda n: "https://thumbnail-%d" %n)


class ItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Item

    title = factory.Sequence(lambda n: "title-%d" % n)
    description = factory.Sequence(lambda n: "description-%d" % n)
    link = factory.Sequence(lambda n: "https://link-%d" % n)
    resource = factory.SubFactory(ResourceFactory)


class UserItemsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserItems

    item = factory.SubFactory(ItemFactory)
    access_level = factory.Iterator(ACCESS_LEVEL_CHOICES)
    user_id = 1


class RequestFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Request

    user_id = 1
    item = factory.SubFactory(ItemFactory)
    access_level = factory.Iterator(ACCESS_LEVEL_CHOICES)
    description = factory.Sequence(lambda n: 'description-%d' % n)
    status = StatusLevelEnum.PENDING.value
