import pytest
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation

@pytest.mark.django_db
def test_get_total_resources_count(create_resource):

    #Arrange
    resources_count = 1

    resource_storage = ResourceStorageImplementation()

    #Act
    actual_resources_count = resource_storage.get_total_resources_count()

    #Assert
    assert actual_resources_count == resources_count
