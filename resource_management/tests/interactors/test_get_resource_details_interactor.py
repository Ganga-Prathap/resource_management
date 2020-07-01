import pytest
from unittest.mock import create_autospec, patch
from resource_management.interactors.get_resource_details_interactor import \
    GetResourceDetailsInteractor
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.dtos.dtos import ResourceDto
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_resource_details_when_user_is_not_admin_raise_exception(
        get_user_dto_mock):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=False
    )
    get_user_dto_mock.return_value = userdto
    user_id = 1
    resource_id = 1

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetResourceDetailsInteractor(
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
    presenter.unauthorized_user.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_resource_details_with_invalid_resource_id_raise_exception(
        get_user_dto_mock):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=True
    )
    get_user_dto_mock.return_value = userdto
    user_id = 1
    resource_id = -1

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.is_valid_resource_id.return_value = False
    presenter.invalid_resource_id.side_effect = NotFound

    interactor = GetResourceDetailsInteractor(
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
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.invalid_resource_id.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_resource_details_with_valid_details(
        get_user_dto_mock, resource_dto):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=True
    )
    get_user_dto_mock.return_value = userdto
    user_id = 1
    resource_id = 1

    expected_resource_dict = {
        "resource_id": 1,
        "resource_name": 'github',
        "description": 'it has repository',
        "link": 'https://github.com',
        "thumbnail": 'https://github'
    }

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.get_resource_details.return_value = resource_dto
    presenter.get_resource_details_response.return_value = \
        expected_resource_dict

    interactor = GetResourceDetailsInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    actual_resource_dict = interactor.get_resource_details(
        user_id=user_id,
        resource_id=resource_id
    )

    #Assert
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.get_resource_details_response.assert_called_with(
        resourcedto=resource_dto
    )

    assert actual_resource_dict == expected_resource_dict
