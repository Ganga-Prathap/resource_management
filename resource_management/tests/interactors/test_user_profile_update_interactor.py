import pytest
from unittest.mock import create_autospec
from resource_management.interactors.user_profile_update_interactor import \
    UserProfileUpdateInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.dtos.dtos import UserDto
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_user_profile_update_with_invalid_user():

    #Assert
    user_id = -1
    username = 'GangaPrathap'
    email = 'ganga@gmail.com'
    job_role = 'backend_developer'
    department = 'Technical'
    gender = 'Male'
    profile_pic = 'https://prathap.profile'

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_valid_user.return_value = False
    presenter.invalid_user.side_effect = BadRequest

    interactor = UserProfileUpdateInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.user_profile_update(
        user_id=user_id,
        username=username,
        email=email,
        job_role=job_role,
        department=department,
        gender=gender,
        profile_pic=profile_pic
    )

    #Assert
    user_storage.is_valid_user.assert_called_with(user_id=user_id)
    presenter.invalid_user.assert_called_once()


def test_user_profile_update_with_valid_user(user_dto):

    #Arrange
    user_id = 1
    username = 'GangaPrathap'
    email = 'ganga@gmail.com'
    job_role = 'backend_developer'
    department = 'Technical'
    gender = 'Male'
    profile_pic = 'https://prathap.profile'


    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_valid_user.return_value = True
    user_storage.user_profile_update.return_value = user_dto

    interactor = UserProfileUpdateInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    #Act
    interactor.user_profile_update(
        user_id=user_id,
        username=username,
        email=email,
        job_role=job_role,
        department=department,
        gender=gender,
        profile_pic=profile_pic
    )

    #Assert
    user_storage.is_valid_user.assert_called_with(user_id=user_id)
    user_storage.user_profile_update(
        user_id=user_id,
        username=username,
        email=email,
        job_role=job_role,
        department=department,
        gender=gender,
        profile_pic=profile_pic
    )
