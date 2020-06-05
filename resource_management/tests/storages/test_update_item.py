import pytest
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.models.item import Item


@pytest.mark.django_db
def test_update_item(create_resource, create_item):

    #Arrange
    item_id = 1

    title = 'item1.0'
    description = 'item_description1.0'
    link = 'https://item1.0'

    item_storage = ItemStorageImplementation()

    #Act
    item_storage.update_item(
        item_id=item_id,
        title=title,
        description=description,
        link=link
    )

    #Assert
    item_obj = Item.objects.get(id=item_id)
    assert item_obj.title == title
    assert item_obj.description == description
    assert item_obj.link == link
