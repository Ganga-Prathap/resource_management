import pytest
from resource_management_auth.storages.storage_implementation import \
    StorageImplementation
from resource_management_auth.exceptions.exceptions import InvalidPassword

@pytest.mark.django_db
def test_invalid_password_raise_exception(create_user):

    #Arrange
    username = 'Ganesh'
    password = '123wa'

    storage_implement = StorageImplementation()

    #Act
    with pytest.raises(InvalidPassword):
        storage_implement.validate_password(
            username=username,
            password=password
        )

@pytest.mark.django_db
def test_valid_password(create_user):

    #Arrange
    username = 'Ganesh'
    password = 'rgukt123'
    user_id = 1

    storage_implement = StorageImplementation()

    #Act
    return_user_id = storage_implement.validate_password(
        username=username,
        password=password
    )

    #Assert
    assert return_user_id == user_id
