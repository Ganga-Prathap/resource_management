from typing import List
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.models.resource import Resource
from resource_management.models.item import Item, UserItems


from resource_management.dtos.dtos import ItemDto


class ItemStorageImplementation(ItemStorageInterface):

    def _get_item_dto(self, item_obj, resource_name):

        item_dto = ItemDto(
            item_id=item_obj.id,
            title=item_obj.title,
            resource_name=resource_name,
            description=item_obj.description,
            link=item_obj.link
        )

        return item_dto

    def create_item(self, resource_id: int,
                    title: str,
                    description: str,
                    link: str) -> ItemDto:

        Item.objects.create(
            title=title,
            description=description,
            link=link,
            resource_id=resource_id
        )

    def get_resource_items(self, resource_id: int,
                           offset: int, limit: int) -> List[ItemDto]:

        resource_obj = Resource.objects.get(id=resource_id)
        resource_name = resource_obj.resource_name
        item_objs = resource_obj.item_set.all()[offset:offset+limit]

        items_dto_list = []

        for item_obj in item_objs:
            item_dto = self._get_item_dto(item_obj, resource_name)
            items_dto_list.append(item_dto)

        return items_dto_list

    def get_resource_items_count(self, resource_id: int) -> int:
        resource_obj = Resource.objects.get(id=resource_id)
        items_count= resource_obj.item_set.all().count()
        return items_count

    def is_valid_item_id(self, item_id: int) -> bool:

        response = Item.objects.filter(id=item_id).exists()
        return response

    def get_item_details(self, item_id: int) -> ItemDto:

        item_obj = Item.objects.select_related('resource').get(id=item_id)
        resource_name = item_obj.resource.resource_name
        item_dto = self._get_item_dto(item_obj, resource_name)
        return item_dto

    def update_item(self, item_id: int,
                    title: str,
                    description: str,
                    link: str) -> ItemDto:

        Item.objects.filter(id=item_id).update(
            title=title,
            description=description,
            link=link
        )

    def delete_items(self, item_ids: List[int]):

        Item.objects.filter(id__in=item_ids).delete()

    """
    def get_user_items(self, user_id: int,
                       offset: int, limit: int) -> List[ItemDto]:

        user_obj = User.objects.get(id=user_id)
        item_objs = user_obj.item_set.all()[offset:offset+limit]

        items_dto_list = []

        for item_obj in item_objs:
            resource_name = item_obj.resource.resource_name
            item_dto = self._get_item_dto(item_obj, resource_name)
            items_dto_list.append(item_dto)

        return items_dto_list

    def get_user_items_count(self, user_id: int) -> int:
        user_obj = User.objects.get(id=user_id)
        items_count = user_obj.item_set.all().count()
        return items_count
    """

    

    def get_user_items(self, user_id: int,
                       offset: int, limit: int) -> List[ItemDto]:

        item_ids = UserItems.objects.filter(
            user_id=user_id).values_list('item_id', flat=True)[offset:offset+limit]

        item_objs = Item.objects.filter(id__in=item_ids)

        items_dto_list = []

        for item_obj in item_objs:
            resource_name = item_obj.resource.resource_name
            item_dto = self._get_item_dto(item_obj, resource_name)
            items_dto_list.append(item_dto)

        return items_dto_list

    def get_user_items_count(self, user_id: int) -> int:
        items_count = UserItems.objects.filter(
            user_id=user_id).count()
        return items_count
