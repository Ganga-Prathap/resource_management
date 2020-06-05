import pytest
from unittest.mock import create_autospec
from resource_management.interactors.update_password_interactor import \
    UpdatePasswordInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound


def test_update_password_with_invalid_user():

    #Arrange
    user_id = -1
    password = '12345'

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_valid_user.return_value = False
    presenter.invalid_user.side_effect = NotFound

    interactor = UpdatePasswordInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.update_password(
            user_id=user_id,
            password=password
        )

    #Assert
    user_storage.is_valid_user.assert_called_with(user_id=user_id)
    presenter.invalid_user.assert_called_once()


def test_update_password_with_valid_details():

    #Arrange
    user_id = 1
    password = 'asdfg'

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UpdatePasswordInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    #Act
    interactor.update_password(
        user_id=user_id,
        password=password
    )

    #Assert
    user_storage.is_valid_user.assert_called_with(user_id=user_id)
    user_storage.update_password.assert_called_with(
        user_id=user_id,
        password=password
    )
