import pytest
from unittest.mock import create_autospec
from resource_management.interactors.get_admin_resources_interactor import \
    GetAdminResourcesInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
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

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidOffsetValue.side_effect = BadRequest

    interactor = GetAdminResourcesInteractor(
        user_storage=user_storage,
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

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidLimitValue.side_effect = BadRequest

    interactor = GetAdminResourcesInteractor(
        user_storage=user_storage,
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

def test_get_admin_resources_when_user_is_not_admin_raise_exception():

    #Arrange
    user_id = 1
    offset = 0
    limit = 1

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetAdminResourcesInteractor(
        user_storage=user_storage,
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
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.unauthorized_user.assert_called_once()


def test_get_admin_resources_when_user_is_admin(admin_resources_dto):

    #Arrange
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

    user_storage = create_autospec(UserStorageInterface)
    resource_storage = create_autospec(ResourceStorageInterface)
    presenter = create_autospec(PresenterInterface)

    resource_storage.get_total_resources_count.return_value = resources_count
    resource_storage.get_admin_resources.return_value = admin_resources_dto
    presenter.get_admin_resources_response.return_value = \
        expected_resources_dict

    interactor = GetAdminResourcesInteractor(
        user_storage=user_storage,
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
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    resource_storage.get_admin_resources.assert_called_with(
        offset=offset,
        limit=limit
    )
    presenter.get_admin_resources_response.assert_called_with(
        resources_list_dto=admin_resources_dto,
        resources_count=resources_count
    )
    assert actual_resources_list == expected_resources_dict
