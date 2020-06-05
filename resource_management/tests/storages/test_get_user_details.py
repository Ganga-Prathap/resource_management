import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.dtos.dtos import UserDto


@pytest.mark.django_db
def test_get_user_details(user_dto):

    #Arrange
    user_id = 1

    expected_user_dto = UserDto(
        user_id=1,
        username='Prathap',
        email='prathap@gmail.com',
        job_role='backend_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://prathap.profile'
    )

    storage_implement = UserStorageImplementation()

    #Act
    actual_user_dto = storage_implement.get_user_details(
        user_id=user_id
    )

    #Assert
    assert actual_user_dto == expected_user_dto
