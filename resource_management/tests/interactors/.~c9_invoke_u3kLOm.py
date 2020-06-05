import pytest
from unittest.mock import create_autospec
from resource_management.interactors.get_users_interactor import \
    GetUsersInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest





def test_get_users_when_user_is_not_admin_raise_exception():

    #Arragne
    user_id = 1
    offset = 0
    limit = 1

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_users(
            user_id=user_id,
            offset=offset,
            limit=limit
        )


def test_get_users_with_valid_details(user_dto):

    #Arrange
    user_id = 2
    offset = 0
    limit = 1
    users_dto = [user_dto]

    expected_user_dict = [{
        'user_id': 1,
        'username': 'Prathap',
        'email': 'prathap@gmail.com',
        'job_role': 'backend_developer',
        'department': 'Technical',
        'gender': 'Male',
        'profile_pic': 'https://prathap.profile'
    }]

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.get_users.return_value = users_dto
    presenter.get_users_response.return_value = expected_user_dict

    interactor = GetUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    #Act
    users_dict = interactor.get_users(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.get_users_response.assert_called_with(
        users_dto=users_dto
    )
    assert users_dict == expected_user_dict
