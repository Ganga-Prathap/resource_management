import pytest
from unittest.mock import create_autospec
from resource_management.interactors.get_resource_details_interactor import \
    GetResourceDetailsInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.dtos.dtos import ResourceDto
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)


def test_get_resource_details_when_user_is_not_admin_raise_exception():

    #Arrange
    user_id = 1
    resource_id = 1

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetResourceDetailsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_resource_details(
            user_id=user_id,
            resource_id=resource_id
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.unauthorized_user.assert_called_once()


def test_get_resource_details_with_invalid_resource_id_raise_exception():

    #Arrange
    user_id = 1
    resource_id = -1

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.is_valid_resource_id.return_value = False
    presenter.invalid_resource_id.side_effect = NotFound

    interactor = GetResourceDetailsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_resource_details(
            user_id=user_id,
            resource_id=resource_id
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.invalid_resource_id.assert_called_once()


def test_get_resource_details_with_valid_details(resource_dto):

    #Arrange
    user_id = 1
    resource_id = 1

    expected_resource_dict = {
        "resource_id": 1,
        "resource_name": 'github',
        "description": 'it has repository',
        "link": 'https://github.com',
        "thumbnail": 'https://github'
    }

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.get_resource_details.return_value = resource_dto
    presenter.get_resource_details_response.return_value = \
        expected_resource_dict

    interactor = GetResourceDetailsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    actual_resource_dict = interactor.get_resource_details(
        user_id=user_id,
        resource_id=resource_id
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.get_resource_details_response.assert_called_with(
        resourcedto=resource_dto
    )

    assert actual_resource_dict == expected_resource_dict
