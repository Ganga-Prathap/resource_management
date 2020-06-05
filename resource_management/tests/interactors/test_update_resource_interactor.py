from unittest.mock import create_autospec
import pytest
from resource_management.interactors.update_resource_interactor import \
    UpdateResourceInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound


def test_update_resource_when_user_is_not_admin_raise_exception():

    #Arrange
    user_id = 1
    resource_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.user_not_allowed_to_update_resource.side_effect = BadRequest

    interactor = UpdateResourceInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.update_resource(
            user_id=user_id,
            resource_id=resource_id,
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.user_not_allowed_to_update_resource.assert_called_once()


def test_update_test_with_invalid_resource_id_raise_exception():

    #Arrange
    user_id = 1
    resource_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.is_valid_resource_id.return_value = False
    presenter.invalid_resource_id.side_effect = NotFound

    interactor = UpdateResourceInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.update_resource(
            user_id=user_id,
            resource_id=resource_id,
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.invalid_resource_id.assert_called_once()


def test_update_resource_with_valid_details(resource_dto):

    #Arrange
    user_id = 1
    resource_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'


    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    #resource_storage.update_resource.return_value = resource_dto

    interactor = UpdateResourceInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    interactor.update_resource(
        user_id=user_id,
        resource_id=resource_id,
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    resource_storage.update_resource(
        resource_id=resource_id,
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )
