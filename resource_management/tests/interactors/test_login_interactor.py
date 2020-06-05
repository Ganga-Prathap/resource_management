import datetime
from unittest.mock import create_autospec
from unittest.mock import patch
import pytest
from resource_management.interactors.login_interactor import \
    LoginInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.oauth2_storage import OAuth2SQLStorage
from resource_management.exceptions.exceptions import InvalidPassword
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)


def test_login_with_invalid_username_raise_exception():

    #Arrange
    username = 'Naveen'
    password = '12345'

    user_storage = create_autospec(UserStorageInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorage)
    presenter = create_autospec(PresenterInterface)

    user_storage.validate_username.return_value = False
    presenter.username_not_exists.side_effect = NotFound

    interactor = LoginInteractor(
        user_storage=user_storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.login(
            username=username,
            password=password
        )

    #Assert
    user_storage.validate_username.assert_called_with(
        username=username
    )
    presenter.username_not_exists.assert_called_once()

def test_login_with_invalid_password_raise_exception():

    #Arrange
    username = 'Prathap'
    password = '123aq'

    user_storage = create_autospec(UserStorageInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorage)
    presenter = create_autospec(PresenterInterface)

    user_storage.validate_username.return_value = True
    user_storage.validate_password.side_effect = InvalidPassword
    presenter.invalid_password.side_effect = BadRequest

    interactor = LoginInteractor(
        user_storage=user_storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.login(
            username=username,
            password=password
        )

    #Assert
    user_storage.validate_username.assert_called_with(username=username)
    user_storage.validate_password.assert_called_with(
        username=username,
        password=password
    )
    presenter.invalid_password.assert_called_once()

given_tokens = \
    UserAuthTokensDTO(
        user_id=1,
        access_token='rMeGKBv7qe64IounsrgMXXKbVkrN5U',
        refresh_token='s0lsy47ybxjQfmelr22Sp03DOuqzhg',
        expires_in=datetime.datetime(2023, 7, 28, 20, 10, 14, 724033)
    )


@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens',
              return_value=given_tokens)
def test_login_with_valid_details(create_user_auth_tokens_mock):

    #Arrange
    username = 'Prathap'
    password = '12345'
    user_id = 1
    is_admin = False
    expected_tokens = {
        'access_token': 'rMeGKBv7qe64IounsrgMXXKbVkrN5U',
        'is_admin': False
    }


    user_storage = create_autospec(UserStorageInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorage)
    presenter = create_autospec(PresenterInterface)

    user_storage.validate_username.return_value = True
    user_storage.validate_password.return_value = user_id
    user_storage.is_user_admin_or_not.return_value = False
    presenter.get_tokens_service.return_value = expected_tokens

    interactor = LoginInteractor(
        user_storage=user_storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )

    #Act
    tokens = interactor.login(
        username=username,
        password=password
    )

    #Assert
    user_storage.validate_username.assert_called_with(username=username)
    user_storage.validate_password.assert_called_with(
        username=username,
        password=password
    )
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.get_tokens_service.assert_called_with(
        token=given_tokens,
        is_admin=is_admin
    )

    assert tokens == expected_tokens
