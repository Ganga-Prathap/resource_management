from unittest.mock import create_autospec, patch
import pytest
from resource_management.interactors.create_resource_interactor import \
    CreateResourcesInteractor
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.dtos.dtos import ResourceDto
from django_swagger_utils.drf_server.exceptions import BadRequest


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_create_resource_when_user_not_admin_raise_exception(get_user_dto_mock):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=False
    )
    get_user_dto_mock.return_value = userdto
    user_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.user_not_allowed_to_create_resource.side_effect = BadRequest

    interactor = CreateResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.create_resource(
            user_id=user_id,
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )
    #Assert
    presenter.user_not_allowed_to_create_resource.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_create_resource_when_user_is_admin(get_user_dto_mock):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=True
    )
    get_user_dto_mock.return_value = userdto
    user_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    interactor.create_resource(
        user_id=user_id,
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )

    #Assert
    resource_storage.create_resource.assert_called_with(
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_create_resource_when_user_id_is_invalid(get_user_dto_mock):

    #Arrange
    from resource_management.exceptions.exceptions import InvalidUserId
    get_user_dto_mock.side_effect = InvalidUserId

    user_id = 1
    resource_name = 'github'
    description = 'it has repository'
    link = 'https://github.com'
    thumbnail = 'https://github'

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(InvalidUserId):
        interactor.create_resource(
            user_id=user_id,
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )
