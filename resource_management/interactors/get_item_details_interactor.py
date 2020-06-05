from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetItemDetailsInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 item_storage: ItemStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.item_storage = item_storage
        self.presenter = presenter

    def get_item_details(self, user_id: int, item_id: int):

        is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            self.presenter.unauthorized_user()
            return
        is_valid_item = self.item_storage.is_valid_item_id(
            item_id=item_id
        )
        is_not_valid_item = not is_valid_item
        if is_not_valid_item:
            self.presenter.invalid_item_id()
            return

        item_dto = self.item_storage.get_item_details(
            item_id=item_id
        )

        response = self.presenter.get_item_details_response(
            item_dto=item_dto
        )
        return response
