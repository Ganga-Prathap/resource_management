from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetUserInfoInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_user_info(self, user_id: int):

        self.validate_user(user_id)

        user_dto = self.storage.get_user_info(
            user_id=user_id
        )

        user_dict = self.presenter.get_user_info_response(
            userdto=user_dto
        )
        return user_dict

    def validate_user(self, user_id: int):
        is_user_valid = self.storage.is_valid_user(user_id=user_id)
        is_not_valid_user = not is_user_valid
        if is_not_valid_user:
            self.presenter.raise_exception_for_invalid_user_id()
            return
