from typing import List
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.exceptions.exceptions import InvalidItemIds


class GetItems:

    def __init__(self, item_storage: ItemStorageInterface):
        self.item_storage = item_storage

    def get_items_wrapper(self, item_ids: List[int],
                          presenter: PresenterInterface):
        try:
            self.get_items_response(item_ids=item_ids,
                                    presenter=presenter)
        except InvalidItemIds as error:
            presenter.raise_exception_for_invalid_item_ids(error)

    def get_items_response(self, item_ids: List[int],
                           presenter: PresenterInterface):
        items_dto = self.get_items(item_ids=item_ids)
        return presenter.get_items_response(items_dto)

    def get_items(self, item_ids: List[int]):
        item_ids = list(set(item_ids))

        #TODO: VALIDATE ITEM IDS
        self._validate_item_ids(item_ids)

        #TODO: GET ITEMS DTOS
        items_dto = self.item_storage.get_items(item_ids)
        return items_dto

    def _validate_item_ids(self, item_ids):
        valid_item_ids = self.item_storage.get_valid_item_ids(item_ids)
        invalid_item_ids = [
            item_id
            for item_id in item_ids
            if item_id not in valid_item_ids
        ]

        if invalid_item_ids:
            raise InvalidItemIds(invalid_item_ids)
