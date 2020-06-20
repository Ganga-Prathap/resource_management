import pytest
from unittest.mock import create_autospec
from resource_management.interactors.get_items import GetItems
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound


def test_invalid_item_ids_raise_exception():

    #Arrange
    item_ids = [1, 2, 3]
    valid_item_ids = [1, 2]
    invalid_item_ids = [3]

    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_valid_item_ids.return_value = valid_item_ids
    presenter.raise_exception_for_invalid_item_ids.side_effect = NotFound

    interactor = GetItems(item_storage=item_storage)

    #Act
    with pytest.raises(NotFound):
        interactor.get_items_wrapper(
            item_ids=item_ids,
            presenter=presenter
        )

    #Assert
    item_storage.get_valid_item_ids.assert_called_once_with(item_ids)
    call_obj = presenter.raise_exception_for_invalid_item_ids.call_args
    error_obj = call_obj.args[0]
    assert error_obj.item_ids == invalid_item_ids


def test_get_items(items_dto):

    #Arrange
    item_ids = [1, 2]

    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_valid_item_ids.return_value = item_ids
    item_storage.get_items.return_value = items_dto

    interactor = GetItems(item_storage=item_storage)

    #Act
    interactor.get_items_wrapper(
        item_ids=item_ids,
        presenter=presenter)

    #Assert
    item_storage.get_valid_item_ids.assert_called_once_with(item_ids)
    item_storage.get_items.assert_called_once_with(item_ids)
    presenter.get_items_response.assert_called_once_with(items_dto)
