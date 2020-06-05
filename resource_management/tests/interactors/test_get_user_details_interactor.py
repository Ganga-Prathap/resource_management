import pytest
from unittest.mock import create_autospec
from resource_management.interactors.get_user_details_interactor import \
    GetUserDetailsInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_get_user_details_with_invalid_user_raise_exception():

    #Arrange
    user_id = -1

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_valid_user.return_value = False
    presenter.invalid_user.side_effect = BadRequest

    interactor = GetUserDetailsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_user_details(
            user_id=user_id
        )

    #Assert
    user_storage.is_valid_user.assert_called_with(user_id=user_id)
    presenter.invalid_user.assert_called_once()


def test_get_user_details_with_valid_user(user_dto):

    #Arrange
    user_id = 1

    expected_user_dict = {
        'user_id': 1,
        'username': 'Prathap',
        'email': 'prathap@gmail.com',
        'job_role': 'backend_developer',
        'department': 'Technical',
        'gender': 'Male',
        'profile_pic': 'https://prathap.profile'
    }

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.get_user_details.return_value = user_dto
    presenter.get_user_details_response.return_value = expected_user_dict

    interactor = GetUserDetailsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    #Act
    actual_user_dict = interactor.get_user_details(
        user_id=user_id
    )

    #Assert
    user_storage.is_valid_user.assert_called_with(
        user_id=user_id
    )
    user_storage.get_user_details.assert_called_with(
        user_id=user_id
    )
    presenter.get_user_details_response.assert_called_with(
        user_dto=user_dto
    )

    assert actual_user_dict == expected_user_dict
