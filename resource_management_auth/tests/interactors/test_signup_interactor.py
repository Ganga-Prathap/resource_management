import datetime
from unittest.mock import create_autospec
from unittest.mock import patch
import pytest
from resource_management_auth.interactors.signup_interactor import \
    SignupInteractor
from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_signup_with_username_already_exist_raise_exception():

    #Arrange
    username = 'Prathap'
    password = '12345'

    storage = create_autospec(StorageInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorage)
    presenter = create_autospec(PresenterInterface)

    storage.validate_username.return_value = True
    presenter.raise_exception_for_username_already_exist.side_effect = \
        BadRequest

    interactor = SignupInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.signup(
            username=username,
            password=password
        )

    #Assert
    storage.validate_username.assert_called_with(username=username)
    presenter.raise_exception_for_username_already_exist.assert_called_once()


given_tokens = \
    UserAuthTokensDTO(
        user_id=1,
        access_token='rMeGKBv7qe64IounsrgMXXKbVkrN5U',
        refresh_token='s0lsy47ybxjQfmelr22Sp03DOuqzhg',
        expires_in=datetime.datetime(2023, 7, 28, 20, 10, 14, 724033)
    )


@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens',
              return_value=given_tokens)
def test_signup_with_valid_details(create_user_auth_tokens_mock):

    #Arrange
    username = 'Ganga'
    password = 'asdfg'
    user_id = 2
    is_admin = False
    expected_tokens = {
        'access_token': 'rMeGKBv7qe64IounsrgMXXKbVkrN5U',
        'is_admin': False
    }

    storage = create_autospec(StorageInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorage)
    presenter = create_autospec(PresenterInterface)

    storage.validate_username.return_value = False
    storage.signup_new_user.return_value = user_id
    storage.is_user_admin_or_not.return_value = False
    presenter.get_tokens_service.return_value = expected_tokens

    interactor = SignupInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )

    #Act
    tokens = interactor.signup(
        username=username,
        password=password
    )

    #Assert
    storage.validate_username.assert_called_with(username=username)
    storage.signup_new_user.assert_called_with(
        username=username,
        password=password
    )
    presenter.get_tokens_service.assert_called_with(
        token=given_tokens,
        is_admin=is_admin
    )
    assert tokens == expected_tokens
