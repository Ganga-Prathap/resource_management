import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.exceptions.exceptions import InvalidPassword

@pytest.mark.django_db
def test_invalid_password_raise_exception(create_user):

    #Arrange
    username = 'Ganesh'
    password = '123wa'

    user_storage_implement = UserStorageImplementation()

    #Act
    with pytest.raises(InvalidPassword):
        user_storage_implement.validate_password(
            username=username,
            password=password
        )

@pytest.mark.django_db
def test_valid_password(create_user):

    #Arrange
    username = 'Ganesh'
    password = 'rgukt123'
    user_id = 1

    user_storage_implement = UserStorageImplementation()

    #Act
    return_user_id = user_storage_implement.validate_password(
        username=username,
        password=password
    )

    #Assert
    assert return_user_id == user_id
