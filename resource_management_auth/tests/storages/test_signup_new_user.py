import pytest
from resource_management_auth.storages.storage_implementation import \
    StorageImplementation

@pytest.mark.django_db
def test_signup_new_user():

    #Arragne
    username = 'Naveen'
    password = 'asdfg'
    expected_user_id = 1

    storage = StorageImplementation()

    #Act
    actual_user_id = storage.signup_new_user(
        username=username,
        password=password
    )

    #Assert
    assert actual_user_id == expected_user_id
