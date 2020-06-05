from unittest.mock import create_autospec
import pytest
from resource_management.interactors.create_resource_interactor import \
    CreateResourcesInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.dtos.dtos import ResourceDto
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_create_resource_when_user_not_admin_raise_exception():

    #Arrange
    user_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.user_not_allowed_to_create_resource.side_effect = BadRequest

    interactor = CreateResourcesInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.create_resource(
            user_id=user_id,
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )
    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.user_not_allowed_to_create_resource.assert_called_once()


def test_create_resource_when_user_is_admin():

    #Arrange
    user_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'

    

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = True

    interactor = CreateResourcesInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    interactor.create_resource(
        user_id=user_id,
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.create_resource.assert_called_with(
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )
