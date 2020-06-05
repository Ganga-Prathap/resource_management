import pytest
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.dtos.dtos import ItemDto
@pytest.mark.django_db
def test_get_items_of_resource(create_resource, create_item):

    #Arrange
    resource_id = 1
    offset = 0
    limit = 1
    expected_item_dto = [
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
    actual_item_dto = item_storage.get_resource_items(
        resource_id=resource_id,
        offset=offset,
        limit=limit
    )

    #Assert
    assert actual_item_dto == expected_item_dto
