import pytest
from unittest.mock import create_autospec
from resource_management.interactors.get_item_details_interactor import \
    GetItemDetailsInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.dtos.dtos import ItemDto
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound


def test_get_item_details_when_user_is_not_admin_raise_exception():

#Arrange
    user_id = 1
    item_id = 1

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = NotFound

    interactor = GetItemDetailsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_item_details(
            user_id=user_id,
            item_id=item_id
        )
    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.unauthorized_user.assert_called_once()


def test_get_item_details_with_invalid_item_id_raise_exception():

    #Arrange
    user_id = 1
    item_id = -1

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.is_valid_item_id.return_value = False
    presenter.invalid_item_id.side_effect = NotFound

    interactor = GetItemDetailsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_item_details(
            user_id=user_id,
            item_id=item_id
        )
    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    item_storage.is_valid_item_id.assert_called_with(item_id=item_id)
    presenter.invalid_item_id.assert_called_once()


def test_get_items_details_with_valid_details(item_dto):

    #Arragne
    user_id = 1
    item_id = 1

    expected_item_dict = {
        'item_id': 1,
        'title': 'item1',
        'resource_name': 'github',
        'description': 'item_description',
        'link': 'https://item1'
    }

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_item_details.return_value = item_dto
    presenter.get_item_details_response.return_value = expected_item_dict

    interactor = GetItemDetailsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    actual_item_dict = interactor.get_item_details(
        user_id=user_id,
        item_id=item_id
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    item_storage.is_valid_item_id.assert_called_with(
        item_id=item_id
    )
    presenter.get_item_details_response.assert_called_with(
        item_dto=item_dto
    )
    assert actual_item_dict == expected_item_dict
