from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetAdminResourcesInteractor:

    def __init__(self, resource_storage: ResourceStorageInterface,
                 presenter: PresenterInterface):
        self.resource_storage = resource_storage
        self.presenter = presenter

    def get_admin_resources(self, user_id: int,
                            offset:int,
                            limit: int):

        self.validate_offset_value(offset)
        self.validate_limit_value(limit)
        self.validate_admin(user_id)

        resources_count = self.resource_storage.get_total_resources_count()
        resources_list_dto = self.resource_storage.get_admin_resources(
            offset=offset, limit=limit
        )
        response = self.presenter.get_admin_resources_response(
            resources_list_dto=resources_list_dto,
            resources_count=resources_count
        )
        return response

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

    def _check_offset_value(self, offset):
        if offset < 0:
            return False
        return True
    def _check_limit_value(self, limit):
        if limit <= 0:
            return False
        return True
