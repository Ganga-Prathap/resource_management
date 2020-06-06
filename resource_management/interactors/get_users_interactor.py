from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetUsersInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_users(self, user_id: int,
                  offset: int,
                  limit: int):

        self.validate_offset_value(offset)
        self.validate_limit_value(limit)
        self.validate_admin(user_id)

        users_count = self.user_storage.get_users_count()
        users_dto = self.user_storage.get_users(
            offset=offset, limit=limit
        )
        users_dict = self.presenter.get_users_response(
            users_dto=users_dto,
            users_count=users_count
        )
        return users_dict

    def validate_admin(self, user_id: int):
        is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)
        is_not_admin = not is_admin
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
        if limit < 0:
            return False
        return True
