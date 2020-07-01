import pytest
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.dtos.dtos import ItemDto


@pytest.mark.django_db
def test_get_user_items(create_resource,
                        create_item,
                        create_useritems):

    #Arrange
    user_id = 1
    offset = 0
    limit = 1
    expected_items_dto = [
        ItemDto(
            item_id=1,
            title='item1',
            resource_name='github',
            description='item_description',
            link='https://item1'
        )
    ]

    item_storage = ItemStorageImplementation()

    #Act
    actual_items_dto = item_storage.get_user_items(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    #Assert
    assert actual_items_dto == expected_items_dto

