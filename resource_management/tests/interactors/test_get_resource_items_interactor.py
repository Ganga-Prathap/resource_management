import pytest
from unittest.mock import create_autospec
from resource_management.interactors.get_resource_items_interactor import \
    GetResourceItemsInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound


def test_get_resource_items_when_offset_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    resource_id = 1
    offset = -1
    limit = 1

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidOffsetValue.side_effect = BadRequest

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_resource_items(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.invalidOffsetValue.assert_called_once()


def test_get_resource_items_when_limit_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    resource_id = 1
    offset = 0
    limit = -1

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidLimitValue.side_effect = BadRequest

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_resource_items(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.invalidLimitValue.assert_called_once()


def test_get_resource_items_when_user_is_not_admin_raise_exception():

    #Arrange
    user_id = 1
    resource_id = 1
    offset = 0
    limit = 1

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_resource_items(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.unauthorized_user.assert_called_once()


def test_get_resource_items_with_invalid_resource_id_raise_exception():

    #Arrange
    user_id = 1
    resource_id = -1
    offset = 0
    limit = 1

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.is_valid_resource_id.return_value = False
    presenter.invalid_resource_id.side_effect = NotFound

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_resource_items(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.invalid_resource_id.assert_called_once()


def test_get_resource_items_with_valid_details(item_dto):

    #Arrange
    user_id = 1
    resource_id = 1
    offset = 0
    limit = 1
    items_count = 1
    items_dto = [item_dto]
    expected_items_dict = {
        "total_items": items_count,
        "items": [{
            'item_id': 1,
            'title': 'item1',
            'resource_name': 'github',
            'description': 'item_description',
            'link': 'https://item1'
        }]
    }

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_resource_items.return_value = items_dto
    item_storage.get_resource_items_count.return_value = items_count
    presenter.get_resource_items_response.return_value = expected_items_dict

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    actual_items_dict = interactor.get_resource_items(
        user_id=user_id,
        resource_id=resource_id,
        offset=offset,
        limit=limit
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    item_storage.get_resource_items.assert_called_with(
        resource_id=resource_id, offset=offset, limit=limit
    )
    presenter.get_resource_items_response.assert_called_with(
        items_dto_list=items_dto,
        items_count=items_count
    )
    assert actual_items_dict == expected_items_dict


def test_get_resource_items_when_no_items():

    #Arrange
    user_id = 1
    resource_id = 1
    offset = 0
    limit = 1
    items_count = 0
    items_dto = []
    expected_items_dict = []

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_resource_items.return_value = items_dto
    item_storage.get_resource_items_count.return_value = items_count
    presenter.get_resource_items_response.return_value = expected_items_dict

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    #Act
    actual_items_dict = interactor.get_resource_items(
        user_id=user_id,
        resource_id=resource_id,
        offset=offset,
        limit=limit
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    item_storage.get_resource_items.assert_called_with(
        resource_id=resource_id, offset=offset, limit=limit
    )
    presenter.get_resource_items_response.assert_called_with(
        items_dto_list=items_dto,
        items_count=items_count
    )
    assert actual_items_dict == expected_items_dict
