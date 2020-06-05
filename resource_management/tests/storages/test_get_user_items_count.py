import pytest
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_get_user_items_count(normal_user, create_resource,
                              create_item, item_to_user):

    #Arrange
    user_id = 1
    expected_items_count = 1

    item_storage = ItemStorageImplementation()

    #Act
    actual_items_count = item_storage.get_user_items_count(user_id=user_id)

    #Assert
    assert actual_items_count == expected_items_count
