import pytest
from unittest.mock import create_autospec
from resource_management.interactors.delete_items_interactor import \
    DeleteItemsInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)


def test_delete_items_when_user_is_not_admin_raise_exception():

    #Arrange
    user_id = 1
    item_ids = [1]

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = BadRequest

    interactor = DeleteItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.delete_items(
            user_id=user_id,
            item_ids=item_ids
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.unauthorized_user.assert_called_once()


def test_delete_items_with_invalid_item_ids_raise_exception():

    #Arrange
    user_id = 1
    item_id = -1
    item_ids = [-1]

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.is_valid_item_id.return_value = False
    presenter.invalid_item_id.side_effect = NotFound

    interactor = DeleteItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.delete_items(
            user_id=user_id,
            item_ids=item_ids
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    item_storage.is_valid_item_id.assert_called_with(item_id=item_id)
    presenter.invalid_item_id.assert_called_once()


def test_delete_items_with_valid_details():

    #Arrange
    user_id = 1
    item_id = 1
    item_ids = [1]

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)


    interactor = DeleteItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    interactor.delete_items(
        user_id=user_id,
        item_ids=item_ids
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    item_storage.is_valid_item_id.assert_called_with(item_id=item_id)
    item_storage.delete_items.assert_called_with(
        item_ids=item_ids
    )
