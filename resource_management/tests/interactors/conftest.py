import pytest
import datetime
from resource_management.constants.enums import AccessLevelEnum
from django.contrib.auth.hashers import make_password
from resource_management.models.user import User
from resource_management.dtos.dtos import ResourceDto
from resource_management.dtos.dtos import RequestDto
from resource_management.dtos.dtos import ItemDto
from resource_management.dtos.dtos import UserDto


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
def resource_dto():
    resource_dto = ResourceDto(
        resource_id=1,
        resource_name='github',
        description='it has repository',
        link='https://github.com',
        thumbnail='https://github'
    )
    return resource_dto

@pytest.fixture
def admin_resources_dto():
    resource_dto = [ResourceDto(
        resource_id=1,
        resource_name='github',
        description='it has repository',
        link='https://github.com',
        thumbnail='https://github',
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
def admin_request_dto():
    request_dto = [
        RequestDto(
            request_id=1,
            username='Prathap',
            profile_pic='https://prathap.profile',
            resource_name='resource1',
            item_name='item1',
            access_level=AccessLevelEnum.READ.value,
            due_date_time=datetime.datetime(2020, 6, 1, 0, 0)
        )
    ]
    return request_dto


@pytest.fixture
def items_dto():
    item_dto = [
        ItemDto(
            item_id=1,
            title='item1',
            resource_name='github',
            description='item_description',
            link='https://item1'
        ),
        ItemDto(
            item_id=2,
            title='item2',
            resource_name='github2',
            description='item2_description',
            link='https://item2'
        )
    ]
    return item_dto

@pytest.fixture
def resource_items_dto():
    item_dto = [
        ItemDto(
            item_id=1,
            title='item1',
            resource_name='github',
            description='item_description',
            link='https://item1'
        ),
        ItemDto(
            item_id=2,
            title='item2',
            resource_name='github',
            description='item2_description',
            link='https://item2'
        )
    ]
    return item_dto

"""


@pytest.fixture
def admin_resource_dto():
    resource_dto = ResourceDto(
        resource_id=1,
        resource_name='github',
        description='it has repository',
        link='https://github.com',
        thumbnail='https://github',
    )
    return resource_dto

@pytest.fixture()
def create_item():
    item_dto = ItemDto(
        item_id=1,
        title='item1',
        resource_name='github',
        description='item_description',
        link='https://item1'
    )
    return item_dto


@pytest.fixture()
def create_user():

    users = [
        {
            'username': 'Prathap',
            'name': 'Prathap',
            'password': '12345a'
        },
        {
            'username': 'Naveen',
            'name': 'Naveen',
            'password': '12345'
        }
    ]

    User.objects.bulk_create([
        User(username=user['username'],
             name=user['name'],
             password=make_password(user['password'])
            )
        for user in users
    ])

@pytest.fixture
def resource_dtos():
    resource_dto = ResourceDto(
        resource_name='github',
        description='it has repository',
        link='https://github.com',
        thumbnail='https://github',
    )
    return resource_dto
"""
