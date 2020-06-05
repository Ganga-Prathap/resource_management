import pytest
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.models.item import Item


@pytest.mark.django_db
def test_delete_items(create_resource, create_item):

    #Arrange
    item_ids = [1]

    item_storage = ItemStorageImplementation()

    #Act
    item_storage.delete_items(
        item_ids=item_ids
    )

    #Assert
    with pytest.raises(Item.DoesNotExist):
        Item.objects.get(id=item_ids[0])
