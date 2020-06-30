from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from resource_management_auth.dtos.dtos import UserDto


class PresenterInterface:

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def get_tokens_service(self, token: UserAuthTokensDTO,
                           is_admin: bool):
        pass

    @abstractmethod
    def raise_exception_for_username_already_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_id(self):
        pass
