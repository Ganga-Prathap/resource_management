from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class UpdatePasswordInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def update_password(self, user_id: int,
                        password: str):

        is_user_valid = self.user_storage.is_valid_user(user_id=user_id)
        is_not_valid_user = not is_user_valid
        if is_not_valid_user:
            self.presenter.invalid_user()
        self.user_storage.update_password(
            user_id=user_id,
            password=password
        )
