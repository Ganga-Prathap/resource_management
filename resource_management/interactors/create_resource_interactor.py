from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class CreateResourcesInteractor:

    def __init__(self, resource_storage: ResourceStorageInterface,
                 presenter: PresenterInterface):
        self.resource_storage = resource_storage
        self.presenter = presenter

    def create_resource(self, user_id: int,
                        resource_name: str,
                        description: str,
                        link: str,
                        thumbnail: str):
        
        self.validate_admin(user_id)

        self.resource_storage.create_resource(
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )

    def validate_admin(self, user_id: int):
        from resource_management.adapters.service_adapter import \
            get_service_adapter
        service_adapter = get_service_adapter()
        userdto = service_adapter.auth_service.get_user_details(user_id)
        is_not_admin = not userdto.is_admin
        if is_not_admin:
            self.presenter.user_not_allowed_to_create_resource()
            return
