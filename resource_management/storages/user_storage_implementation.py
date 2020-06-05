from typing import Optional, List
from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.exceptions.exceptions import (
    UserDoesNotExist,
    InvalidPassword
)
from resource_management.dtos.dtos import UserDto
from resource_management.models.user import User
from resource_management.models.item import Item


class UserStorageImplementation(UserStorageInterface):

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

    def is_valid_user(self, user_id: int) -> bool:
        response = User.objects.filter(id=user_id).exists()
        return response

    def _get_user_dto(self, user_obj):
        user_dto = UserDto(
            user_id=user_obj.id,
            username=user_obj.username,
            email=user_obj.email,
            job_role=user_obj.job_role,
            department=user_obj.department,
            gender=user_obj.gender,
            profile_pic=user_obj.profile_pic
        )
        return user_dto

    def get_user_details(self, user_id: int) -> UserDto:
        user_obj = User.objects.get(id=user_id)
        user_dto = self._get_user_dto(user_obj)
        return user_dto

    def user_profile_update(self, user_id: int, username: str,
                            email: str, job_role: str,
                            department: str, gender: str,
                            profile_pic: str) -> UserDto:
        User.objects.filter(id=user_id).update(
            username=username, email=email, job_role=job_role,
            department=department, gender=gender, profile_pic=profile_pic
        )
        user_obj = User.objects.get(id=user_id)
        user_dto = self._get_user_dto(user_obj)
        return user_dto

    def get_item_users(self, item_id: int) -> List[UserDto]:
        item_obj = Item.objects.get(id=item_id)
        user_objs = item_obj.users.all()

        user_dto_list = []
        for user_obj in user_objs:
            user_dto = self._get_user_dto(user_obj)
            user_dto_list.append(user_dto)
        return user_dto_list

    def update_password(self, user_id: int, password: str):
        User.objects.filter(id=user_id).update(
            password=password
        )

    def get_users(self, offset: int, limit: int) -> List[UserDto]:
        user_objs = User.objects.filter(is_admin=False)
        user_objs = user_objs[offset:offset+limit]
        users_dto_list = []
        for user_obj in user_objs:
            user_dto = self._get_user_dto(user_obj)
            users_dto_list.append(user_dto)
        return users_dto_list

    def get_users_count(self) -> int:
        users_count = User.objects.filter(is_admin=False).count()
        return users_count
