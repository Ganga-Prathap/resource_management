import pytest
import datetime
from unittest.mock import create_autospec
from resource_management.interactors.get_admin_requests_interactor import \
    GetAdminRequestsInteractor
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
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

    user_storage = create_autospec(UserStorageInterface)
    request_storage = create_autospec(RequestStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidOffsetValue.side_effect = BadRequest

    interactor = GetAdminRequestsInteractor(
        user_storage=user_storage,
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

    user_storage = create_autospec(UserStorageInterface)
    request_storage = create_autospec(RequestStorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.invalidLimitValue.side_effect = BadRequest

    interactor = GetAdminRequestsInteractor(
        user_storage=user_storage,
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


def test_get_admin_requests_when_user_is_not_admin_raise_exception():

    user_id = 1
    offset = 0
    limit = 1

    user_storage = create_autospec(UserStorageInterface)
    request_storage = create_autospec(RequestStorageInterface)
    presenter = create_autospec(PresenterInterface)

    user_storage.is_user_admin_or_not.return_value = False
    presenter.unauthorized_user.side_effect = BadRequest

    interactor = GetAdminRequestsInteractor(
        user_storage=user_storage,
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
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    presenter.unauthorized_user.assert_called_once()


def test_get_admin_requests_with_valid_details(admin_request_dto):

    #Arrange
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
                'profile_pic': 'https://prathap.profile',
                'resource_name': 'resource1',
                'item_name': 'item1',
                'access_level': AccessLevelEnum.READ.value,
                'due_date_time': datetime.datetime(2020, 6, 1, 0, 0)
            }
        ]
    }

    user_storage = create_autospec(UserStorageInterface)
    request_storage = create_autospec(RequestStorageInterface)
    presenter = create_autospec(PresenterInterface)

    request_storage.get_admin_requests.return_value = request_dto_list
    request_storage.get_total_requests_count.return_value = total_count
    presenter.get_admin_requests_response.return_value = \
        expected_request_dict

    interactor = GetAdminRequestsInteractor(
        user_storage=user_storage,
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
    user_storage.is_user_admin_or_not.assert_called_with(user_id=user_id)
    request_storage.get_admin_requests.assert_called_with(
        offset=offset, limit=limit
    )
    presenter.get_admin_requests_response.assert_called_with(
        requests_dto=request_dto_list, total_requests=total_count
    )
    assert actual_requested_dict == expected_request_dict
