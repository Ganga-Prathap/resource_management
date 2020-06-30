import pytest
from resource_management_auth.storages.storage_implementation import \
    StorageImplementation


@pytest.mark.django_db
def test_user_is_admin(admin_user):

    #Arrange
    user_id = 1
    is_admin = True

    storage = StorageImplementation()

    #Act
    response = storage.is_user_admin_or_not(user_id=user_id)

    #Assert
    assert response == is_admin

@pytest.mark.django_db
def test_user_is_not_admin(normal_user):

    #Arrange
    user_id = 1
    is_admin = False

    storage = StorageImplementation()

    #Act
    response = storage.is_user_admin_or_not(user_id=user_id)

    #Assert
    assert response == is_admin
