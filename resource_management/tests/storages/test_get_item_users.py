import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.dtos.dtos import UserDto


@pytest.mark.django_db
def test_get_item_users(create_user, create_resource, create_item,
                        item_to_user):

    #Assert
    item_id = 1
    expected_users_dto = [UserDto(
        user_id=1,
        username='Ganesh',
        email='ganesh@gmail.com',
        job_role='front_developer',
        department='Technical',
        gender='Male',
        profile_pic='https://ganesh.profile'
    )]

    user_storage = UserStorageImplementation()

    #Act
    actula_users_dto = user_storage.get_item_users(
        item_id=item_id
    )

    #Assert
    assert actula_users_dto == expected_users_dto
