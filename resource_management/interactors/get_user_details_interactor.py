from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetUserDetailsInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_user_details(self, user_id: int):

        self.validate_user(user_id)

        user_dto = self.user_storage.get_user_details(
            user_id=user_id
        )

        user_dict = self.presenter.get_user_details_response(
            user_dto=user_dto
        )
        return user_dict

    def validate_user(self, user_id: int):
        is_user_valid = self.user_storage.is_valid_user(user_id=user_id)
        is_not_valid_user = not is_user_valid
        if is_not_valid_user:
            self.presenter.invalid_user()
            return
