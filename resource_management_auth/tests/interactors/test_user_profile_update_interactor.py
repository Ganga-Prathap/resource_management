import pytest
from unittest.mock import create_autospec
from resource_management_auth.interactors.user_profile_update_interactor import \
    UserProfileUpdateInteractor
from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management_auth.dtos.dtos import UserInfoDto
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

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_valid_user.return_value = False
    presenter.raise_exception_for_invalid_user_id.side_effect = BadRequest

    interactor = UserProfileUpdateInteractor(
        storage=storage,
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
    storage.is_valid_user.assert_called_with(user_id=user_id)
    presenter.raise_exception_for_invalid_user_id.assert_called_once()


def test_user_profile_update_with_valid_user():

    #Arrange
    user_id = 1
    username = 'GangaPrathap'
    email = 'ganga@gmail.com'
    job_role = 'backend_developer'
    department = 'Technical'
    gender = 'Male'
    profile_pic = 'https://prathap.profile'


    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UserProfileUpdateInteractor(
        storage=storage,
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
    storage.is_valid_user.assert_called_with(user_id=user_id)
    storage.user_profile_update(
        user_id=user_id,
        username=username,
        email=email,
        job_role=job_role,
        department=department,
        gender=gender,
        profile_pic=profile_pic
    )
