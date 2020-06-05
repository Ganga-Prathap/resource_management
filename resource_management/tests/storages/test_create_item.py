import pytest
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.models.item import Item

@pytest.mark.django_db
def test_create_item(create_resource):

    #Arrange
    item_id = 1
    resource_id = 1
    title = 'item1'
    description = 'item_description'
    link = 'https://item1'


    item_storage = ItemStorageImplementation()

    #Act
    item_storage.create_item(
        resource_id=resource_id,
        title=title,
        description=description,
        link=link
    )

    #Assert
    item_obj = Item.objects.get(id=item_id)
    assert item_obj.resource_id == resource_id
    assert item_obj.title == title
    assert item_obj.description == description
    assert item_obj.link == link
