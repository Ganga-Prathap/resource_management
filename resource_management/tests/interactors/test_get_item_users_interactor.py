import pytest
from unittest.mock import create_autospec, patch
from resource_management.interactors.get_item_users_interactor import \
    GetItemUsersInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound


def test_get_item_users_when_user_is_not_admin_raise_exception():

    #Arrange
    user_id = 1
    item_id = 1

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetItemUsersInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_item_users(
            user_id=user_id,
            item_id=item_id
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.unauthorized_user.assert_called_once()


def test_get_item_users_with_invalid_item_id_raise_exception():

    #Arrange
    user_id = 1
    item_id = -1

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.is_valid_item_id.return_value = False
    presenter.invalid_item_id.side_effect = NotFound

    interactor = GetItemUsersInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_item_users(
            user_id=user_id,
            item_id=item_id
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    item_storage.is_valid_item_id.assert_called_with(item_id=item_id)
    presenter.invalid_item_id.assert_called_once()


def test_get_item_users_with_valid_details(user_dto):

    #Arrange
    user_id = 1
    item_id = 1

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
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.get_item_users.return_value = users_dto
    presenter.get_item_users_response.return_value = expected_user_dict

    interactor = GetItemUsersInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    actual_users_dict = interactor.get_item_users(
        user_id=user_id,
        item_id=item_id
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    item_storage.is_valid_item_id.assert_called_with(item_id=item_id)
    user_storage.get_item_users.assert_called_with(item_id=item_id)
    presenter.get_item_users_response.assert_called_with(
        users_dto=users_dto
    )
    assert actual_users_dict == expected_user_dict
