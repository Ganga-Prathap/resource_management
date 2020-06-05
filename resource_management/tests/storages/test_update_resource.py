import pytest
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.models.resource import Resource


@pytest.mark.django_db
def test_update_resource(create_resource):

    #Arrange
    resource_id = 1
    resource_name = 'github2'
    description = 'it has repository2'
    link = 'https://github.com2'
    thumbnail = 'https://github2'


    resource_storage = ResourceStorageImplementation()

    #Act
    resource_storage.update_resource(
        resource_id=resource_id,
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )

    #Assert
    resource_obj = Resource.objects.get(id=resource_id)
    assert resource_obj.resource_name == resource_name
    assert resource_obj.description == description
    assert resource_obj.link == link
    assert resource_obj.thumbnail == thumbnail
