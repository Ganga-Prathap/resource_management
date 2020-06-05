import pytest
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.dtos.dtos import UserDto
from resource_management.models.user import User


@pytest.mark.django_db
def test_user_profile_update(user_dto):

    #Arrange
    user_id = 1
    username = 'GangaPrathap'
    email = 'gangaprathap@gmail.com'
    job_role = 'backend_developer'
    department = 'Technical'
    gender = 'Male'
    profile_pic = 'https://prathap.profile'


    user_storage = UserStorageImplementation()

    #Act
    user_storage.user_profile_update(
        user_id=user_id,
        username=username,
        email=email,
        job_role=job_role,
        department=department,
        gender=gender,
        profile_pic=profile_pic
    )

    #Assert
    user_obj = User.objects.get(id=user_id)
    assert user_obj.username == username
    assert user_obj.email == email
    assert user_obj.job_role == job_role
    assert user_obj.department == department
    assert user_obj.gender == gender
    assert user_obj.profile_pic == profile_pic
