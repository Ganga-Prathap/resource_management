from abc import abstractmethod
from typing import Optional
from resource_management_auth.dtos.dtos import UserDto


class StorageInterface:

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
    def get_user_details(self, user_id) -> Optional[UserDto]:
        pass
