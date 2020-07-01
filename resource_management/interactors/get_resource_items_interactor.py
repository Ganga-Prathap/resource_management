from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetResourceItemsInteractor:

    def __init__(self, resource_storage: ResourceStorageInterface,
                 item_storage: ItemStorageInterface,
                 presenter: PresenterInterface):
        self.resource_storage = resource_storage
        self.item_storage = item_storage
        self.presenter = presenter

    def get_resource_items(self, user_id: int,
                           resource_id: int,
                           offset: int,
                           limit: int):

        self.validate_offset_value(offset)
        self.validate_limit_value(limit)
        self.validate_admin(user_id)
        self.validate_resource(resource_id)

        items_count = self.item_storage.get_resource_items_count(
            resource_id=resource_id
        )
        items_dto_list = self.item_storage.get_resource_items(
            resource_id=resource_id, offset=offset, limit=limit
        )
        items_dict_list = self.presenter.get_resource_items_response(
            items_dto_list=items_dto_list,
            items_count=items_count
        )
        return items_dict_list

    def validate_admin(self, user_id: int):
        from resource_management.adapters.service_adapter import \
            get_service_adapter
        service_adapter = get_service_adapter()
        userdto = service_adapter.auth_service.get_user_details(user_id)
        is_not_admin = not userdto.is_admin
        if is_not_admin:
            self.presenter.unauthorized_user()
            return

    def validate_offset_value(self, offset: int):
        is_offset_valid = self._check_offset_value(offset)
        is_offset_invalid = not is_offset_valid
        if is_offset_invalid:
            self.presenter.invalidOffsetValue()
            return

    def validate_limit_value(self, limit: int):
        is_limit_valid = self._check_limit_value(limit)
        is_limit_invalid = not is_limit_valid
        if is_limit_invalid:
            self.presenter.invalidLimitValue()
            return

    def validate_resource(self, resource_id: int):
        is_valid_resource = self.resource_storage.is_valid_resource_id(
            resource_id=resource_id
        )
        is_not_valid_resource = not is_valid_resource
        if is_not_valid_resource:
            self.presenter.invalid_resource_id()
            return

    def _check_offset_value(self, offset):
        if offset < 0:
            return False
        return True

    def _check_limit_value(self, limit):
        if limit < 0:
            return False
        return True
