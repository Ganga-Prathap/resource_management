from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class GetAdminResourcesInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 resource_storage: ResourceStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.resource_storage = resource_storage
        self.presenter = presenter

    def get_admin_resources(self, user_id: int, offset:int, limit: int):

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

        is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            self.presenter.unauthorized_user()
            return
        resources_count = self.resource_storage.get_total_resources_count()
        resources_list_dto = self.resource_storage.get_admin_resources(
            offset=offset, limit=limit
        )
        response = self.presenter.get_admin_resources_response(
            resources_list_dto=resources_list_dto,
            resources_count=resources_count
        )
        return response

    def _check_offset_value(self, offset):
        if offset < 0:
            return False
        return True
    def _check_limit_value(self, limit):
        if limit < 0:
            return False
        return True
