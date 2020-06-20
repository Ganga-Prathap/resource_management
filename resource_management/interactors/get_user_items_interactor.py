from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.exceptions.exceptions import (
    InvalidOffsetException,
    InvalidLimitException,
    InvalidUserException
)
from resource_management.interactors.validation_mixer import \
    ValidationMixer


class GetUserItemsInteractor(ValidationMixer):

    def __init__(self, user_storage: UserStorageInterface,
                 item_storage: ItemStorageInterface):
        self.user_storage = user_storage
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
                presenter=presenter
            )
        except InvalidOffsetException as error:
            presenter.raise_exception_for_invalid_offset_value(error)
        except InvalidLimitException as error:
            presenter.raise_exception_for_invalid_limit_value(error)
        except InvalidUserException as error:
            presenter.raise_exception_for_invalid_user(error)

    def get_user_items_response(self, user_id: int,
                                offset: int,
                                limit: int,
                                presenter: PresenterInterface):
        user_items_dto, items_count = self.get_user_items(user_id=user_id,
                                        offset=offset,
                                        limit=limit)
        user_items_dict = presenter.get_user_items_response(
            items_dto=user_items_dto,
            items_count=items_count
        )
        return user_items_dict

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
