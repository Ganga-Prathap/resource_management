import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation

@pytest.mark.django_db
def test_invalid_username():

    #Assert
    username = 'Naveen'
    expected_response = False

    user_storage_implement = UserStorageImplementation()

    #Act
    actual_response = user_storage_implement.validate_username(
        username=username
    )

    #Assert
    assert actual_response == expected_response

@pytest.mark.django_db
def test_valid_username(create_user):

    #Assert
    username = create_user.username
    expected_response = True

    user_storage_implement = UserStorageImplementation()

    #Act
    actual_response = user_storage_implement.validate_username(
        username=username
    )

    #Assert
    assert actual_response == expected_response
