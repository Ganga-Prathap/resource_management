import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.models.user import User


@pytest.mark.django_db
def test_update_password(user_dto):

    #Arrange
    user_id = 1
    password = 'asdfg'

    user_storage = UserStorageImplementation()

    #Act
    user_storage.update_password(
        user_id=user_id,
        password=password
    )

    #Assert
    user_obj = User.objects.get(id=user_id)
    assert user_obj.password == password
