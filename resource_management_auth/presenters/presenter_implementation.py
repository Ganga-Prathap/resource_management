from resource_management_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from common.dtos import UserAuthTokensDTO
from resource_management_auth.dtos.dtos import UserDto
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)
from resource_management_auth.constants.exception_message import (
    USER_DOES_NOT_EXISTS,
    INVALID_PASSWORD,
    USER_NAME_ALREADY_EXIST,
    INVALID_USER
)


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_username(self):
        raise NotFound(*USER_DOES_NOT_EXISTS)

    def raise_exception_for_invalid_password(self):
        raise BadRequest(*INVALID_PASSWORD)

    def get_tokens_service(self, token: UserAuthTokensDTO,
                           is_admin: bool):
        return {
            'access_token': token.access_token,
            'is_admin': is_admin
        }

    def raise_exception_for_username_already_exist(self):
        raise BadRequest(*USER_NAME_ALREADY_EXIST)

    def raise_exception_for_invalid_user_id(self):
        raise NotFound(*INVALID_USER)
