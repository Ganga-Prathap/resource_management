import pytest
from unittest.mock import create_autospec
from resource_management.interactors.update_item_interactor import \
    UpdateItemInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.dtos.dtos import ItemDto
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound


def test_update_item_when_user_is_not_admin_raise_exception():

    #Arrange
    user_id = 1
    item_id = 1

    title = 'item1.0'
    description = 'item_description1.0'
    link = 'https://item1.0'

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = BadRequest

    interactor = UpdateItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.update_item(
            user_id=user_id,
            item_id=item_id,
            title=title,
            description=description,
            link=link
        )
    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.unauthorized_user.assert_called_once()


def test_update_item_with_invalid_item_id_raise_exception(resource_dto):

    #Arrange
    user_id = 1
    item_id = -1

    title = 'item1.0'
    description = 'item_description1.0'
    link = 'https://item1.0'

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    item_storage.is_valid_item_id.return_value = False
    presenter.invalid_item_id.side_effect = NotFound

    interactor = UpdateItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.update_item(
            user_id=user_id,
            item_id=item_id,
            title=title,
            description=description,
            link=link
        )

    #Assert
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    item_storage.is_valid_item_id.assert_called_with(
        item_id=item_id
    )
    presenter.invalid_item_id.assert_called_once()


def test_update_item_with_valid_details(resource_dto, item_dto):

    #Arrange
    user_id = 1
    item_id = 1

    title = 'item1.0'
    description = 'item_description1.0'
    link = 'https://item1.0'

    expected_item_dto = ItemDto(
        item_id=1,
        title='item1.0',
        resource_name='github',
        description='item_description1.0',
        link='https://item1.0'
    )

    user_storage = create_autospec(UserStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)


    interactor = UpdateItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    interactor.update_item(
        user_id=user_id,
        item_id=item_id,
        title=title,
        description=description,
        link=link
    )

    #Arrange
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    item_storage.is_valid_item_id.assert_called_with(
        item_id=item_id
    )
    item_storage.update_item.assert_called_with(
        item_id=item_id,
        title=title,
        description=description,
        link=link
    )
