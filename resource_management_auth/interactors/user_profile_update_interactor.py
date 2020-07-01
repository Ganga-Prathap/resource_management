from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface import \
    PresenterInterface


class UserProfileUpdateInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def user_profile_update(self, user_id: int,
                            username: str,
                            email: str,
                            job_role: str,
                            department: str,
                            gender: str,
                            profile_pic: str):

        self.validate_user(user_id)

        self.storage.user_profile_update(
            user_id=user_id,
            username=username,
            email=email,
            job_role=job_role,
            department=department,
            gender=gender,
            profile_pic=profile_pic
        )

    def validate_user(self, user_id: int):
        is_user_valid = self.storage.is_valid_user(user_id=user_id)
        is_not_valid_user = not is_user_valid
        if is_not_valid_user:
            self.presenter.raise_exception_for_invalid_user_id()
            return
