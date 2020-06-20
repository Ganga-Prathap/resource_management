import pytest
from unittest.mock import create_autospec, patch
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
from resource_management.interactors.get_items import GetItems
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound


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
    presenter.raise_exception_for_unauthorized_user.side_effect = BadRequest

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage,
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_resource_items_wrapper(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.raise_exception_for_unauthorized_user.assert_called_once()


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
    presenter.raise_exception_for_invalid_resource_id.side_effect = NotFound

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage
    )

    #Act
    with pytest.raises(NotFound):
        interactor.get_resource_items_wrapper(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.raise_exception_for_invalid_resource_id.assert_called_once()


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

    presenter.raise_exception_for_invalid_offset_value.side_effect = BadRequest

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_resource_items_wrapper(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.raise_exception_for_invalid_offset_value.assert_called_once()


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

    presenter.raise_exception_for_invalid_limit_value.side_effect = BadRequest

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_resource_items_wrapper(
            user_id=user_id,
            resource_id=resource_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.raise_exception_for_invalid_limit_value.assert_called_once()


@patch.object(GetItems, 'get_items')
def test_get_resource_items_with_valid_details(get_items_mock,
                                               resource_items_dto):

    #Arrange
    get_items_mock.return_value = resource_items_dto
    user_id = 1
    resource_id = 1
    offset = 0
    limit = 2
    items_count = 2,
    item_ids = [1, 2]

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_resource_items_count.return_value = items_count
    item_storage.get_resource_item_ids.return_value = item_ids

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage
    )

    #Act
    interactor.get_resource_items_wrapper(
        user_id=user_id,
        resource_id=resource_id,
        offset=offset,
        limit=limit,
        presenter=presenter
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    item_storage.get_resource_items_count.assert_called_once_with(resource_id)
    item_storage.get_resource_item_ids.assert_called_with(
        resource_id=resource_id, offset=offset, limit=limit
    )
    presenter.get_resource_items_response.assert_called_with(
        items_dto=resource_items_dto,
        items_count=items_count
    )


@patch.object(GetItems, 'get_items')
def test_get_resource_items_when_no_items(get_items_mock):

    #Arrange
    get_items_mock.return_value = []
    user_id = 1
    resource_id = 1
    offset = 0
    limit = 2
    items_count = 0,
    item_ids = []

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.get_resource_items_count.return_value = items_count
    item_storage.get_resource_item_ids.return_value = item_ids

    interactor = GetResourceItemsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        item_storage=item_storage
    )

    #Act
    interactor.get_resource_items_wrapper(
        user_id=user_id,
        resource_id=resource_id,
        offset=offset,
        limit=limit,
        presenter=presenter
    )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    item_storage.get_resource_items_count.assert_called_once_with(resource_id)
    item_storage.get_resource_item_ids.assert_called_with(
        resource_id=resource_id, offset=offset, limit=limit
    )
    presenter.get_resource_items_response.assert_called_with(
        items_dto=[],
        items_count=items_count
    )
