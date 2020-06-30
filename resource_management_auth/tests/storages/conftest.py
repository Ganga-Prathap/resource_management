import pytest
import datetime
from django.contrib.auth.hashers import make_password
from resource_management_auth.models.user import User
from freezegun import freeze_time


@pytest.fixture
def create_user():

    user_obj = User.objects.create_user(
        username='Ganesh',
        password='rgukt123',
        is_admin=True,
        email='ganesh@gmail.com',
        job_role='front_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://ganesh.profile'
    )
    return user_obj


@pytest.fixture
def admin_user():
    User.objects.create_user(
        username='Ganesh',
        password='rgukt123',
        is_admin=True,
        email='ganesh@gmail.com',
        job_role='front_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://ganesh.profile'
    )

@pytest.fixture
def normal_user():
    User.objects.create_user(
        username='Prathap',
        password='12345',
        email='prathap@gmail.com',
        job_role='backend_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://prathap.profile'
    )

"""
@pytest.fixture
def user_dto():
    User.objects.create_user(
        username='Prathap',
        password='12345',
        email='prathap@gmail.com',
        job_role='backend_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://prathap.profile'
    )

@pytest.fixture()
def create_resource():
    Resource.objects.create(
        resource_name='github',
        description='it has repository',
        link='https://github.com',
        thumbnail='https://github'
    )

@pytest.fixture
def create_item():
    Item.objects.create(
        title='item1',
        resource_id=1,
        description='item_description',
        link='https://item1'
    )

@pytest.fixture()
def item_to_user():
    item_obj = Item.objects.get(id=1)
    user_obj = User.objects.get(id=1)
    user_obj.item_set.add(item_obj)

@pytest.fixture()
@freeze_time("2020-06-01")
def create_request():
    Request.objects.create(
        user_id=1,
        item_id=1,
        access_level=AccessLevelEnum.READ.value,
        due_date_time=datetime.datetime(2020, 6, 1, 0, 0),
        description='I am interested to learn'
    )

"""


"""



@pytest.fixture()
def create_item():
    Item.objects.create(
        title='item1',
        description='item_description',
        link='https://item1',
        resource_id=1
    )

@pytest.fixture()
def item_to_user():
    item_obj = Item.objects.get(id=1)
    user_obj = User.objects.get(id=1)
    user_obj.item_set.add(item_obj)
"""

"""
@pytest.fixture()
def user():
    User.objects.create_user(
        username='Prathap',
        password='12345',
        is_admin=False,
        email='prathap@gmail.com',
        job_role='backend_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://prathap.profile'
    )
    User.objects.create_user(
        username='Ganesh',
        password='rgukt123',
        is_admin=True,
        email='ganesh@gmail.com',
        job_role='front_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://ganesh.profile'
    )
"""

"""
@pytest.fixture()
def create_user():

    users = [
        {
            'username': 'Prathap',
            'password': '12345a',
            'is_admin': False
        },
        {
            'username': 'Naveen',
            'password': '12345',
            'is_admin': True
        }
    ]

    User.objects.bulk_create([
        User(username=user['username'],
             password=make_password(user['password']),
             is_admin=user['is_admin']
            )
        for user in users
    ])
"""
