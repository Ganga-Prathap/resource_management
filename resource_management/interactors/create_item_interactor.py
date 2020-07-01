from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class CreateItemInteractor:

    def __init__(self, resource_storage: ResourceStorageInterface,
                 item_storage: ItemStorageInterface,
                 presenter: PresenterInterface):
        self.resource_storage = resource_storage
        self.item_storage = item_storage
        self.presenter = presenter

    def create_item(self, user_id: int, resource_id: int, title: str,
                    description: str, link: str):

        self.validate_admin(user_id)
        self.validate_resource(resource_id)
        self.item_storage.create_item(
            resource_id=resource_id,
            title=title,
            description=description,
            link=link
        )

    def validate_admin(self, user_id: int):
        from resource_management.adapters.service_adapter import \
            get_service_adapter
        service_adapter = get_service_adapter()
        userdto = service_adapter.auth_service.get_user_details(user_id)
        is_not_admin = not userdto.is_admin
        if is_not_admin:
            self.presenter.unauthorized_user()
            return

    def validate_resource(self, resource_id: int):
        is_valid_resource = self.resource_storage.is_valid_resource_id(
            resource_id=resource_id
        )
        is_not_valid_resource = not is_valid_resource
        if is_not_valid_resource:
            self.presenter.invalid_resource_id()
            return
