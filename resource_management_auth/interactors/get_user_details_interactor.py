from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management_auth.exceptions.exceptions import InvalidUserId


class GetUserDetails:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_user_details(self, user_id: int):

        try:
            return self.storage.get_user_details(user_id)
        except InvalidUserId:
            self.presenter.raise_exception_for_invalid_user_id()
