import pytest
import datetime
from unittest.mock import patch
from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.constants.enums import AccessLevelEnum
from resource_management.dtos.dtos import RequestDto


@pytest.mark.django_db
def test_get_user_requests(get_user_dto_mock, create_resource,
                           create_item, create_request):

    #Arrange
    offset = 0
    limit = 1
    expected_request_dto = [
        RequestDto(
            request_id=1,
            username='Prathap',
            resource_name='github',
            item_name='item1',
            access_level=AccessLevelEnum.READ.value,
            due_date_time=datetime.datetime(2020, 6, 1, 0, 0)
        )
    ]

    request_storage = RequestStorageImplementation()

    #Act
    actual_request_dto = request_storage.get_admin_requests(
        offset=offset,
        limit=limit
    )

    #Assert
    assert actual_request_dto == expected_request_dto
