import pytest
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.models.resource import Resource
from resource_management.dtos.dtos import ResourceDto

@pytest.mark.django_db
def test_create_resource():

    #Arrange
    resource_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'

    resource_storage = ResourceStorageImplementation()

    #Act
    resource_storage.create_resource(
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )

    #Assert
    resource_obj = Resource.objects.get(id=resource_id)
    assert resource_obj.id == resource_id
    assert resource_obj.resource_name == resource_name
    assert resource_obj.description == description
    assert resource_obj.link == link
    assert resource_obj.thumbnail == thumbnail
