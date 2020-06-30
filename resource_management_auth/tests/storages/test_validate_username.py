import pytest
from resource_management_auth.storages.storage_implementation import \
    StorageImplementation

@pytest.mark.django_db
def test_invalid_username():

    #Assert
    username = 'Naveen'
    expected_response = False

    storage_implement = StorageImplementation()

    #Act
    actual_response = storage_implement.validate_username(
        username=username
    )

    #Assert
    assert actual_response == expected_response

@pytest.mark.django_db
def test_valid_username(create_user):

    #Assert
    username = create_user.username
    expected_response = True

    storage_implement = StorageImplementation()

    #Act
    actual_response = storage_implement.validate_username(
        username=username
    )

    #Assert
    assert actual_response == expected_response
