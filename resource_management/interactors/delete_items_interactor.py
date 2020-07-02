from typing import List
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class DeleteItemsInteractor:

    def __init__(self, item_storage: ItemStorageInterface,
                 presenter: PresenterInterface):

        self.item_storage = item_storage
        self.presenter = presenter

    def delete_items(self, user_id: int,
                     item_ids: List[int]):

        self.validate_admin(user_id)
        for item_id in item_ids:
            is_valid_item = self.item_storage.is_valid_item_id(
                item_id=item_id
            )
            is_not_valid_item = not is_valid_item
            if is_not_valid_item:
                self.presenter.invalid_item_id()
                return
        self.item_storage.delete_items(item_ids=item_ids)

    def validate_admin(self, user_id: int):
        from resource_management.adapters.service_adapter import \
            get_service_adapter
        service_adapter = get_service_adapter()
        userdto = service_adapter.auth_service.get_user_details(user_id)
        is_not_admin = not userdto.is_admin
        if is_not_admin:
            self.presenter.unauthorized_user()
            return
