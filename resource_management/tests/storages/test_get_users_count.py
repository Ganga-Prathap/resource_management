import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation

@pytest.mark.django_db
def test_get_users_count(normal_user):

    #Arrange
    expected_users_count = 1

    user_storage = UserStorageImplementation()

    #Act
    actual_users_count = user_storage.get_users_count()

    #Assert
    assert actual_users_count == expected_users_count
