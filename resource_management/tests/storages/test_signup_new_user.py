import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation

@pytest.mark.django_db
def test_signup_new_user():

    #Arragne
    username = 'Naveen'
    password = 'asdfg'
    expected_user_id = 1

    user_storage = UserStorageImplementation()

    #Act
    actual_user_id = user_storage.signup_new_user(
        username=username,
        password=password
    )

    #Assert
    assert actual_user_id == expected_user_id
