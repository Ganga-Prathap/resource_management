import factory
from datetime import datetime
from resource_management.models.user import User
from resource_management.models.resource import Resource
from resource_management.models.item import Item
from resource_management.models.request import Request
from resource_management.constants.enums import (
    AccessLevelEnum,
    StatusLevelEnum
)

ACCESS_LEVEL_CHOICE=[
            access.value
            for access in AccessLevelEnum
        ]

STATUS_LEVEL_CHOICE=[
            status.value
            for status in StatusLevelEnum
        ]


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "username-%d" % n)
    is_admin = object
    email = factory.LazyAttribute(lambda obj: '%s@email.com' % obj.username)
    job_role = factory.Sequence(lambda n: "job_role-%d" % n)
    department = factory.Sequence(lambda n: "department-%d" % n)
    gender = factory.Iterator(['Male', 'Female'])
    profile_pic = factory.Sequence(lambda n: "profile_pic-%d" % n)

class ResourceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Resource

    resource_name = factory.Sequence(lambda n: "resource_name-%d" % n)
    description = factory.Sequence(lambda n: "description-%d" % n)
    link = factory.Sequence(lambda n: "https://link%d" % n)
    thumbnail = factory.Sequence(lambda n: "https://thumbnail%d" %n)

class ItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Item

    title = factory.Sequence(lambda n: "title-%d" % n)
    description = factory.Sequence(lambda n: "description-%d" % n)
    link = factory.Sequence(lambda n: "https://link%d" % n)
    resource = factory.SubFactory(ResourceFactory)

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for user in extracted:
                self.users.add(user)

class RequestFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Request

    user = factory.SubFactory(UserFactory)
    item = factory.SubFactory(ItemFactory)

    due_date_time = factory.LazyFunction(datetime.now)
    description = factory.Sequence(lambda n: "description-%d" % n)
    access_level = factory.Iterator(ACCESS_LEVEL_CHOICE)
    status = factory.Iterator(STATUS_LEVEL_CHOICE)
