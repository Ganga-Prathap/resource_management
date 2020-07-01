import pytest
from unittest.mock import create_autospec, patch
from resource_management.interactors.create_item_interactor import \
    CreateItemInteractor
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.storages.item_storage_interface import \
    ItemStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_create_item_when_user_is_not_admin_raise_exception(get_user_dto_mock):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=False
    )
    get_user_dto_mock.return_value = userdto
    user_id = -1
    resource_id = 1
    title = 'item1'
    description = 'item_description'
    link = 'https://item1'

    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.unauthorized_user.side_effect = BadRequest

    interactor = CreateItemInteractor(
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.create_item(
            user_id=user_id,
            resource_id=resource_id,
            title=title,
            description=description,
            link=link
        )

    #Assert
    presenter.unauthorized_user.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_create_item_with_invalid_resource_id_raise_exception(get_user_dto_mock):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=True
    )
    get_user_dto_mock.return_value = userdto
    user_id = 1
    resource_id = -1
    title = 'item1'
    description = 'item_description'
    link = 'https://item1'

    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.is_valid_resource_id.return_value = False
    presenter.invalid_resource_id.side_effect = NotFound

    interactor = CreateItemInteractor(
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(NotFound):
        interactor.create_item(
            user_id=user_id,
            resource_id=resource_id,
            title=title,
            description=description,
            link=link
        )

    #Assert
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    presenter.invalid_resource_id.assert_called_once()

@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_create_item_with_valid_details(get_user_dto_mock):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=True
    )
    get_user_dto_mock.return_value = userdto
    user_id = 1
    resource_id = 1
    title = 'item1'
    description = 'item_description'
    link = 'https://item1'

    resource_storage = create_autospec(ResourceStorageInterface)
    item_storage = create_autospec(ItemStorageInterface)
    presenter = create_autospec(PresenterInterface)


    interactor = CreateItemInteractor(
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    #Act
    interactor.create_item(
        user_id=user_id,
        resource_id=resource_id,
        title=title,
        description=description,
        link=link
    )

    #Assert
    resource_storage.is_valid_resource_id.assert_called_with(
        resource_id=resource_id
    )
    item_storage.create_item.assert_called_with(
        resource_id=resource_id,
        title=title,
        description=description,
        link=link
    )
