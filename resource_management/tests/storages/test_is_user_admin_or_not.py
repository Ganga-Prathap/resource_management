import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation


@pytest.mark.django_db
def test_user_is_admin(admin_user):

    #Arrange
    user_id = 1
    is_admin = True

    user_storage = UserStorageImplementation()

    #Act
    response = user_storage.is_user_admin_or_not(user_id=user_id)

    #Assert
    assert response == is_admin

@pytest.mark.django_db
def test_user_is_not_admin(normal_user):

    #Arrange
    user_id = 1
    is_admin = False

    user_storage = UserStorageImplementation()

    #Act
    response = user_storage.is_user_admin_or_not(user_id=user_id)

    #Assert
    assert response == is_admin
