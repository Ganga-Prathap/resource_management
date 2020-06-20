from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.get_items import GetItems
from resource_management.exceptions.exceptions import (
    UnAuthorizedUserException,
    InvalidResourceIdException,
    InvalidOffsetException,
    InvalidLimitException
)
from resource_management.interactors.validation_mixer import ValidationMixer


class GetResourceItemsInteractor(ValidationMixer):

    def __init__(self, user_storage: UserStorageInterface,
                 resource_storage: ResourceStorageInterface,
                 item_storage: ItemStorageInterface):
        self.user_storage = user_storage
        self.resource_storage = resource_storage
        self.item_storage = item_storage

    def get_resource_items_wrapper(self, user_id: int,
                                   resource_id: int,
                                   offset: int,
                                   limit: int,
                                   presenter: PresenterInterface):
        try:
            return self.get_resource_items_response(
                user_id=user_id,
                resource_id=resource_id,
                offset=offset,
                limit=limit,
                presenter=presenter
            )
        except UnAuthorizedUserException as error:
            presenter.raise_exception_for_unauthorized_user(error)
        except InvalidResourceIdException as error:
            presenter.raise_exception_for_invalid_resource_id(error)
        except InvalidOffsetException as error:
            presenter.raise_exception_for_invalid_offset_value(error)
        except InvalidLimitException as error:
            presenter.raise_exception_for_invalid_limit_value(error)

    def get_resource_items_response(self, user_id: int,
                                    resource_id: int,
                                    offset: int,
                                    limit: int,
                                    presenter: PresenterInterface):
        resource_items_dto, items_count = self.get_resource_items(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit
        )
        return presenter.get_resource_items_response(
            resource_items_dto, items_count)

    def get_resource_items(self, user_id: int,
                           resource_id: int,
                           offset: int,
                           limit: int):

        self.validate_admin(user_id)
        self.validate_resource(resource_id)
        self.validate_offset_value(offset)
        self.validate_limit_value(limit)

        items_count = self.item_storage.get_resource_items_count(
            resource_id=resource_id
        )
        item_ids = self.item_storage.get_resource_item_ids(
            resource_id, offset, limit)

        get_items_interactor = GetItems(item_storage=self.item_storage)
        items_dto = get_items_interactor.get_items(item_ids)

        return items_dto, items_count
