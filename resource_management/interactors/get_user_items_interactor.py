from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.exceptions.exceptions import (
    InvalidOffsetValue,
    InvalidLimitValue,
    InvalidUserId
)


class GetUserItemsInteractor:

    def __init__(self, item_storage: ItemStorageInterface):
        self.item_storage = item_storage

    def get_user_items_wrapper(self, user_id: int,
                               offset: int,
                               limit: int,
                               presenter: PresenterInterface):
        try:
            return self.get_user_items_response(
                user_id=user_id,
                offset=offset,
                limit=limit,
                presenter=presenter)
        except InvalidOffsetValue:
            presenter.invalidOffsetValue()
        except InvalidLimitValue:
            presenter.invalidLimitValue()
        except InvalidUserId:
            presenter.invalid_user()

    def get_user_items_response(self, user_id: int,
                                offset: int,
                                limit: int,
                                presenter: PresenterInterface):
        items_dto, items_count = self.get_user_items(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

        items_dict = presenter.get_user_items_response(
            items_dto=items_dto,
            items_count=items_count
        )
        return items_dict

    def get_user_items(self, user_id: int,
                       offset: int,
                       limit: int):

        self.validate_offset_value(offset)
        self.validate_limit_value(limit)
        self.validate_user(user_id)

        items_count = self.item_storage.get_user_items_count(user_id=user_id)
        items_dto = self.item_storage.get_user_items(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

        return items_dto, items_count

    def validate_offset_value(self, offset: int):
        is_offset_valid = self._check_offset_value(offset)
        is_offset_invalid = not is_offset_valid
        if is_offset_invalid:
            raise InvalidOffsetValue

    def validate_limit_value(self, limit: int):
        is_limit_valid = self._check_limit_value(limit)
        is_limit_invalid = not is_limit_valid
        if is_limit_invalid:
            raise InvalidLimitValue

    def validate_user(self, user_id: int):
        from resource_management.adapters.service_adapter import \
            get_service_adapter
        service_adapter = get_service_adapter()
        try:
            service_adapter.auth_service.get_user_details(user_id)
        except InvalidUserId:
            raise InvalidUserId

    def _check_offset_value(self, offset):
        if offset < 0:
            return False
        return True

    def _check_limit_value(self, limit):
        if limit <= 0:
            return False
        return True
