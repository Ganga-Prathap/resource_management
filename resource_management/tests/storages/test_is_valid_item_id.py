import pytest
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_invalid_item_id():

    #Arrange
    item_id = -1
    expected_response = False

    item_storage = ItemStorageImplementation()

    #Act
    actual_response = item_storage.is_valid_item_id(
        item_id=item_id
    )

    #Assert
    assert actual_response == expected_response

@pytest.mark.django_db
def test_valid_item_id(create_resource, create_item):

    #Arrange
    item_id = 1
    expected_response = True

    item_storage = ItemStorageImplementation()

    #Act
    actual_response = item_storage.is_valid_item_id(
        item_id=item_id
    )

    #Assert
    assert actual_response == expected_response
