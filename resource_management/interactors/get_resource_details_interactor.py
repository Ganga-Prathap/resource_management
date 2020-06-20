from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.exceptions.exceptions import (
    UnAuthorizedUserException,
    InvalidResourceIdException
)


class GetResourceDetailsInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 resource_storage: ResourceStorageInterface):
        self.user_storage = user_storage
        self.resource_storage = resource_storage

    def get_resource_details_wrapper(self, user_id: int,
                                     resource_id: int,
                                     presenter: PresenterInterface):
        try:
            self.get_resource_details_response(
                user_id=user_id,
                resource_id=resource_id,
                presenter=presenter)
        except UnAuthorizedUserException as error:
            presenter.raise_exception_for_unauthorized_user(error)
        except InvalidResourceIdException as error:
            presenter.raise_exception_for_invalid_resource_id(error)

    def get_resource_details_response(self, user_id: int,
                                      resource_id: int,
                                      presenter: PresenterInterface):
        resource_dto = self.get_resource_details(user_id=user_id,
                                      resource_id=resource_id)
        response = self.presenter.get_resource_details_response(
            resourcedto=resource_dto
        )
        return response

    def get_resource_details(self, user_id: int,
                             resource_id: int):

        self.validate_admin(user_id)
        self.validate_resource(resource_id)

        resource_dto = self.resource_storage.get_resource_details(
            resource_id=resource_id
        )


    def validate_admin(self, user_id: int):
        is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)
        is_not_admin = not is_admin
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
