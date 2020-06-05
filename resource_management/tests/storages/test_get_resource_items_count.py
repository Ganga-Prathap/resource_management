import pytest
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation

@pytest.mark.django_db
def test_get_resource_items_count(create_resource, create_item):

    #Arrange
    resource_id = 1
    expected_items_count = 1

    item_storage = ItemStorageImplementation()

    #Act
    actual_items_count = item_storage.get_resource_items_count(
        resource_id=resource_id
    )

    #Assert
    assert actual_items_count == expected_items_count
