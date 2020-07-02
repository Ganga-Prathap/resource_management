import pytest
import datetime
from unittest.mock import create_autospec, patch
from resource_management.interactors.get_admin_requests_interactor import \
    GetAdminRequestsInteractor
from resource_management.interactors.storages.request_storage_interface \
    import RequestStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.constants.enums import AccessLevelEnum
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_get_admin_requests_when_offset_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    offset = -1
    limit = 1

    request_storage = create_autospec(RequestStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidOffsetValue.side_effect = BadRequest

    interactor = GetAdminRequestsInteractor(
        request_storage=request_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_admin_requests(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.invalidOffsetValue.assert_called_once()

def test_get_admin_requests_when_limit_value_is_invalid_raise_exception():

    #Arrange
    user_id = 1
    offset = 0
    limit = -1

    request_storage = create_autospec(RequestStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidLimitValue.side_effect = BadRequest

    interactor = GetAdminRequestsInteractor(
        request_storage=request_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_admin_requests(
            user_id=user_id,
            offset=offset,
            limit=limit
        )

    #Assert
    presenter.invalidLimitValue.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_admin_requests_when_user_is_not_admin_raise_exception(
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

    request_storage = create_autospec(RequestStorageInterface)
    presenter = create_autospec(PresenterInterface)


    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetAdminRequestsInteractor(
        request_storage=request_storage,
        presenter=presenter
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.get_admin_requests(
            user_id=user_id,
            offset=offset,
            limit=limit
        )
    #Assert
    presenter.unauthorized_user.assert_called_once()


@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
def test_get_admin_requests_with_valid_details(
        get_user_dto_mock, admin_request_dto):

    #Arrange
    from resource_management.dtos.dtos import UserDto
    userdto1 = UserDto(
        user_id=1,
        username='Nav',
        is_admin=False
    )
    userdto2 = UserDto(
        user_id=2,
        username='Prathap',
        is_admin=False
    )
    get_user_dto_mock.side_effect = [userdto1, userdto2]
    user_id = 1
    offset = 0
    limit = 1
    total_count = 1
    request_dto_list = admin_request_dto

    expected_request_dict = {
            'total_requests': 1,
            'requests': 
        [
            {
                'request_id': 1,
                'username': 'Prathap',
                'resource_name': 'resource1',
                'item_name': 'item1',
                'access_level': AccessLevelEnum.READ.value,
                'due_date_time': datetime.datetime(2020, 6, 1, 0, 0)
            }
        ]
    }

    request_storage = create_autospec(RequestStorageInterface)
    presenter = create_autospec(PresenterInterface)

    request_storage.get_admin_requests.return_value = request_dto_list
    request_storage.get_total_requests_count.return_value = total_count
    presenter.get_admin_requests_response.return_value = \
        expected_request_dict

    interactor = GetAdminRequestsInteractor(
        request_storage=request_storage,
        presenter=presenter
    )

    #Act
    actual_requested_dict = interactor.get_admin_requests(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    #Assert
    assert actual_requested_dict == expected_request_dict
