import pytest
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.models.resource import Resource


@pytest.mark.django_db
def test_delete_resource(create_resource):

    #Arrange
    resource_id = 1

    resource_storage = ResourceStorageImplementation()

    #Act
    resource_storage.delete_resource(
        resource_id=resource_id
    )

    #Assert
    with pytest.raises(Resource.DoesNotExist):
        Resource.objects.get(id=resource_id)
