from abc import abstractmethod
from typing import Optional, List
from .dtos import (
    ResourceDto,
    UserDto,
    ItemDto,
    RequestDto
)
class UserStorageInterface:

    @abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def validate_password(self, username: str, password: str) -> Optional[int]:
        pass

    @abstractmethod
    def is_user_admin_or_not(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def signup_new_user(self, username: str, password: str) -> int:
        pass

    @abstractmethod
    def is_valid_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_details(self, user_id: int) -> UserDto:
        pass

    @abstractmethod
    def user_profile_update(self, user_id: int, username: str,
                            email: str, job_role: str,
                            department: str, gender: str,
                            profile_pic: str) -> UserDto:
        pass

    @abstractmethod
    def get_item_users(self, item_id: int) -> List[UserDto]:
        pass

    @abstractmethod
    def update_password(self, user_id: int, password: str):
        pass

    @abstractmethod
    def get_users(self, offset: int, limit: int) -> List[UserDto]:
        pass

    @abstractmethod
    def get_users_count(self) -> int:
        pass
