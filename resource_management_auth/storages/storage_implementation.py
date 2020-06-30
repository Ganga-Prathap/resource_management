from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.models.user import User
from typing import Optional
from resource_management_auth.exceptions.exceptions import (
    InvalidPassword,
    InvalidUserId
)
from resource_management_auth.dtos.dtos import UserDto


class StorageImplementation(StorageInterface):

    def validate_username(self, username: str) -> bool:
        response = User.objects.filter(username=username).exists()
        return response

    def validate_password(self, username: str, password: str) -> Optional[int]:

        user_obj = User.objects.get(username=username)
        if not user_obj.check_password(password):
            raise InvalidPassword
        return user_obj.id

    def is_user_admin_or_not(self, user_id: int) -> bool:
        user_obj = User.objects.get(id=user_id)
        response = user_obj.is_admin
        return response

    def signup_new_user(self, username: str, password: str) -> int:
        user_obj = User.objects.create_user(
            username=username,
            password=password
        )
        return user_obj.id

    def get_user_details(self, user_id) -> Optional[UserDto]:
        try:
            user_obj = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise InvalidUserId
        else:
            return UserDto(
                user_id=user_obj.id,
                username=user_obj.username,
                is_admin=user_obj.is_admin
            )
