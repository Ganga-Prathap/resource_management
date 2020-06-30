import pytest
from unittest.mock import create_autospec
from resource_management_auth.interactors.get_user_details_interactor import \
    GetUserDetails
from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management_auth.dtos.dtos import UserDto
from resource_management_auth.exceptions.exceptions import InvalidUserId
from django_swagger_utils.drf_server.exceptions import NotFound


def test_raise_error_with_invalid_user_id():

    #Arrange
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_user_details.side_effect = InvalidUserId
    presenter.raise_exception_for_invalid_user_id.side_effect = NotFound

    interactor = GetUserDetails(
        storage=storage, presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_user_details(user_id)

    #Assert
    storage.get_user_details.assert_called_with(user_id)
    presenter.raise_exception_for_invalid_user_id.assert_called_once()


def test_get_user_details():

    #Arrange
    user_id = 1
    user_dto = UserDto(
        user_id=1,
        username='user1',
        is_admin=False
    )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_user_details.return_value = user_dto

    interactor = GetUserDetails(
        storage=storage, presenter=presenter
    )

    #Act
    actual_output = interactor.get_user_details(user_id)

    #Assert
    storage.get_user_details.assert_called_with(user_id)
    assert actual_output == user_dto
