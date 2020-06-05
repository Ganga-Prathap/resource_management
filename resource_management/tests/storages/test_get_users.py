import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.dtos.dtos import UserDto


@pytest.mark.django_db
def test_get_users(user_dto):

    #Arrange
    offset = 0
    limit = 1
    expected_users_dto = [UserDto(
        user_id=1,
        username='Prathap',
        email='prathap@gmail.com',
        job_role='backend_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://prathap.profile'
    )]

    user_storage = UserStorageImplementation()

    #Act
    actual_users_dto = user_storage.get_users(offset=offset, limit=limit)

    #Assert
    assert actual_users_dto == expected_users_dto
