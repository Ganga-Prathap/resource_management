from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetUserItemsInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 item_storage: ItemStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.item_storage = item_storage
        self.presenter = presenter

    def get_user_items(self, user_id: int, offset: int, limit: int):

        is_offset_valid = self._check_offset_value(offset)
        is_offset_invalid = not is_offset_valid
        if is_offset_invalid:
            self.presenter.invalidOffsetValue()
            return
        is_limit_valid = self._check_limit_value(limit)
        is_limit_invalid = not is_limit_valid
        if is_limit_invalid:
            self.presenter.invalidLimitValue()
            return

        is_user_valid = self.user_storage.is_valid_user(user_id=user_id)
        is_not_valid_user = not is_user_valid
        if is_not_valid_user:
            self.presenter.invalid_user()
            return
        items_count = self.item_storage.get_user_items_count(user_id=user_id)
        items_dto = self.item_storage.get_user_items(
            user_id=user_id,
            offset=offset,
            limit=limit
        )
        items_dict = self.presenter.get_user_items_response(
            items_dto=items_dto,
            items_count=items_count
        )
        return items_dict

    def _check_offset_value(self, offset):
        if offset < 0:
            return False
        return True
    def _check_limit_value(self, limit):
        if limit < 0:
            return False
        return True
