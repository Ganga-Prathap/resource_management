import pytest
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.dtos.dtos import ResourceDto


@pytest.mark.django_db
def test_get_resource_details(create_resource):

    #Arrange
    resource_id = 1
    

    expected_resource_dto = ResourceDto(
        resource_id=1,
        resource_name='github',
        description='it has repository',
        link='https://github.com',
        thumbnail='https://github'
    )

    resource_storage = ResourceStorageImplementation()

    #Act
    actual_resource_dto = resource_storage.get_resource_details(
        resource_id=resource_id
    )

    #Assert
    assert actual_resource_dto == expected_resource_dto
