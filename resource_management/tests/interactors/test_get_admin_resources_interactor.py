import pytest
from unittest.mock import create_autospec, patch
from resource_management.interactors.get_admin_resources_interactor import \
    GetAdminResourcesInteractor
from resource_management.interactors.storages.resource_storage_interface \
    import ResourceStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_get_admin_resources_when_offset_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    offset = -1
    limit = 1

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidOffsetValue.side_effect = BadRequest

    interactor = GetAdminResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_admin_resources(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.invalidOffsetValue.assert_called_once()

def test_get_admin_resources_when_limit_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    offset = 0
    limit = -1

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidLimitValue.side_effect = BadRequest

    interactor = GetAdminResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_admin_resources(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.invalidLimitValue.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_admin_resources_when_user_is_not_admin_raise_exception(
        get_user_dto_mock):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=False
    )
    get_user_dto_mock.return_value = userdto
    user_id = 1
    offset = 0
    limit = 1

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetAdminResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_admin_resources(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.unauthorized_user.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_admin_resources_when_user_is_admin(
        get_user_dto_mock, admin_resources_dto):

    #Arrange
    print("1: ")
    from resource_management.dtos.dtos import UserDto
    userdto = UserDto(
        user_id=1,
        username='Nav',
        is_admin=True
    )
    get_user_dto_mock.return_value = userdto
    print(get_user_dto_mock)
    user_id = 1
    offset = 0
    limit = 1
    resources_count = 1
    expected_resources_dict = {
        "total_resources": 1,
        "resources": [{
            "resource_id": 1,
            "resource_name": 'github',
            "description": 'it has repository',
            "link": 'https://github.com',
            "thumbnail": 'https://github'
        }]
    }

    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.get_total_resources_count.return_value = resources_count
    resource_storage.get_admin_resources.return_value = admin_resources_dto
    presenter.get_admin_resources_response.return_value = \
        expected_resources_dict

    interactor = GetAdminResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    #Act
    actual_resources_list = interactor.get_admin_resources(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    #Assert
    resource_storage.get_admin_resources.assert_called_with(
        offset=offset,
        limit=limit
    )
    presenter.get_admin_resources_response.assert_called_with(
        resources_list_dto=admin_resources_dto,
        resources_count=resources_count
    )
    assert actual_resources_list == expected_resources_dict
