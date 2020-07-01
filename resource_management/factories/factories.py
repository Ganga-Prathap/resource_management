import factory
from resource_management.models.resource import Resource
from resource_management.models.item import Item, UserItems
from resource_management.models.request import Request

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
