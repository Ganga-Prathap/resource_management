import pytest
import datetime
from resource_management.dtos.dtos import (
    UserDto,
    ResourceDto,
    ItemDto,
    RequestDto
)
from resource_management.constants.enums import AccessLevelEnum


@pytest.fixture
def user_dto():
    user_dto = UserDto(
        user_id=1,
        username='Prathap',
        email='prathap@gmail.com',
        job_role='backend_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://prathap.profile'
    )
    return user_dto

@pytest.fixture
def admin_resources_dto():
    resource_dto = [ResourceDto(
        resource_id=1,
        resource_name='github',
        description='it has repository',
        link='https://github.com',
        thumbnail='https://github'
    )]
    return resource_dto

@pytest.fixture
def item_dto():
    item_dto = ItemDto(
            item_id=1,
            title='item1',
            resource_name='github',
            description='item_description',
            link='https://item1'
    )
    return item_dto

@pytest.fixture
def request_dto():
    request_dto = [
        RequestDto(
            request_id=1,
            user_id=2,
            resource_name='github',
            item_name='item1',
            access_level=AccessLevelEnum.READ.value,
            due_date_time=datetime.datetime(2020, 6, 1, 0, 0)
        )
    ]
    return request_dto
