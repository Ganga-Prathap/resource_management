import pytest
from unittest.mock import create_autospec, patch
from resource_management.interactors.get_user_items_interactor import \
    GetUserItemsInteractor

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

    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidOffsetValue.side_effect = BadRequest

    interactor = GetUserItemsInteractor(
        item_storage=item_storage
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_user_items_wrapper(
            user_id=user_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Assert
    presenter.invalidOffsetValue.assert_called_once()


def test_get_user_items_when_limit_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    offset = 0
    limit = -1

    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidLimitValue.side_effect = BadRequest

    interactor = GetUserItemsInteractor(
        item_storage=item_storage
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_user_items_wrapper(
            user_id=user_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Assert
    presenter.invalidLimitValue.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_user_items_when_user_id_is_invalid_raise_exception(get_user_dto_mock):

    #Arrange
    from resource_management.exceptions.exceptions import InvalidUserId
    get_user_dto_mock.side_effect = InvalidUserId
    user_id = 1
    offset = 0
    limit = 1

    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalid_user.side_effect = NotFound

    interactor = GetUserItemsInteractor(
        item_storage=item_storage
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_user_items_wrapper(
            user_id=user_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Assert
    presenter.invalid_user.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_user_items_with_valid_details(get_user_dto_mock, item_dto):

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

    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_user_items.return_value = items_dto
    item_storage.get_user_items_count.return_value = items_count
    presenter.get_user_items_response.return_value = expected_items_dict

    interactor = GetUserItemsInteractor(
        item_storage=item_storage
    )

    #Act
    actual_items_dict = interactor.get_user_items_wrapper(
            user_id=user_id,
            offset=offset,
            limit=limit,
            presenter=presenter
    )

    #Assert
    assert actual_items_dict == expected_items_dict
