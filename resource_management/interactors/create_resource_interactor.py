from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface

class CreateResourcesInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 resource_storage: ResourceStorageInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.resource_storage = resource_storage
        self.presenter = presenter

    def create_resource(self, user_id: int, resource_name: str,
                         description: str, link: str, thumbnail: str):

        is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            self.presenter.user_not_allowed_to_create_resource()
            return

        self.resource_storage.create_resource(
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )
