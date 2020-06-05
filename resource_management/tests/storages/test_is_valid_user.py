import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation

@pytest.mark.django_db
def test_invalid_user():

    #Assert
    user_id = 1
    expected_response = False

    user_storage = UserStorageImplementation()

    #Act
    actual_response = user_storage.is_valid_user(
        user_id=user_id
    )

    #Assert
    assert actual_response == expected_response


@pytest.mark.django_db
def test_valid_user(create_user):

    #Assert
    user_id = 1
    expected_response = True

    user_storage = UserStorageImplementation()

    #Act
    actual_response = user_storage.is_valid_user(
        user_id=user_id
    )

    #Assert
    assert actual_response == expected_response
