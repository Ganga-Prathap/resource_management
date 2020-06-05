import pytest
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation


@pytest.mark.django_db
def test_invalid_resource_id():

    #Arrange
    resource_id = -1
    expected_response = False

    resource_storage = ResourceStorageImplementation()

    #Act
    actual_response = resource_storage.is_valid_resource_id(
        resource_id=resource_id
    )

    #Assert
    assert actual_response == expected_response

@pytest.mark.django_db
def test_valid_resource_id(create_resource):

    #Arrange
    resource_id = 1
    expected_response = True

    resource_storage = ResourceStorageImplementation()

    #Act
    actual_response = resource_storage.is_valid_resource_id(
        resource_id=resource_id
    )

    #Assert
    assert actual_response == expected_response
