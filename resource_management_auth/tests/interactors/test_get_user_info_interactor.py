import pytest
from unittest.mock import create_autospec
from resource_management_auth.interactors.get_user_info_interactor import \
    GetUserInfoInteractor
from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management_auth.dtos.dtos import UserInfoDto


def test_get_user_details_with_invalid_user_raise_exception():

    #Arrange
    user_id = -1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_valid_user.return_value = False
    presenter.raise_exception_for_invalid_user_id.side_effect = BadRequest

    interactor = GetUserInfoInteractor(
        storage=storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_user_info(
            user_id=user_id
        )

    #Assert
    storage.is_valid_user.assert_called_with(user_id=user_id)
    presenter.raise_exception_for_invalid_user_id.assert_called_once()


def test_get_user_details_with_valid_user():

    #Arrange
    user_id = 1
    user_dto = UserInfoDto(
        user_id=1,
        username='Prathap',
        email='prathap@gmail.com',
        job_role='backend_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://prathap.profile'
    )

    expected_user_dict = {
        'user_id': 1,
        'username': 'Prathap',
        'email': 'prathap@gmail.com',
        'job_role': 'backend_developer',
        'department': 'Technical',
        'gender': 'Male',
        'profile_pic': 'https://prathap.profile'
    }

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_user_info.return_value = user_dto
    presenter.get_user_info_response.return_value = expected_user_dict

    interactor = GetUserInfoInteractor(
        storage=storage,
        presenter=presenter
    )

    #Act
    actual_user_dict = interactor.get_user_info(
        user_id=user_id
    )

    #Assert
    storage.is_valid_user.assert_called_with(
        user_id=user_id
    )
    storage.get_user_info.assert_called_with(
        user_id=user_id
    )
    presenter.get_user_info_response.assert_called_with(
        userdto=user_dto
    )

    assert actual_user_dict == expected_user_dict

