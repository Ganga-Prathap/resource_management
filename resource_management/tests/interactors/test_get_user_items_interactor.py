import pytest
from unittest.mock import create_autospec
from resource_management.interactors.get_user_items_interactor import \
    GetUserItemsInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound



def test_get_user_items_when_offset_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    offset = -1
    limit = 1

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidOffsetValue.side_effect = BadRequest

    interactor = GetUserItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_user_items(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.invalidOffsetValue.assert_called_once()

def test_get_user_items_when_limit_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    offset = 0
    limit = -1

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidLimitValue.side_effect = BadRequest

    interactor = GetUserItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_user_items(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.invalidLimitValue.assert_called_once()


def test_get_user_items_when_user_id_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    offset = 0
    limit = 1

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_valid_user.return_value = False
    presenter.invalid_user.side_effect = NotFound

    interactor = GetUserItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_user_items(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

    #Assert
    user_storage.is_valid_user.assert_called_with(user_id=user_id)
    presenter.invalid_user.assert_called_once()


def test_get_user_items_with_valid_details(item_dto):

    #Arrange
    user_id = 1
    offset = 0
    limit = 1
    items_count = 1

    items_dto = [item_dto]
    expected_items_dict = {
        "total_items": 1,
        "items": [{
            'item_id': 1,
            'title': 'item1',
            'resource_name': 'github',
            'description': 'item_description',
            'link': 'https://item1'
        }]
    }

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_user_items.return_value = items_dto
    item_storage.get_user_items_count.return_value = items_count
    presenter.get_user_items_response.return_value = expected_items_dict

    interactor = GetUserItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    actual_items_dict = interactor.get_user_items(
            user_id=user_id,
            offset=offset,
            limit=limit
    )

    #Assert
    user_storage.is_valid_user.assert_called_with(user_id=user_id)
    item_storage.get_user_items.assert_called_with(
        user_id=user_id,
        offset=offset,
        limit=limit
    )
    presenter.get_user_items_response.assert_called_with(
        items_dto=items_dto,
        items_count=items_count
    )
    assert actual_items_dict == expected_items_dict
