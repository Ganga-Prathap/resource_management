from resource_management.exceptions.exceptions import (
    InvalidOffsetException,
    InvalidLimitException,
    InvalidUserException,
    UnAuthorizedUserException,
    InvalidResourceIdException
)


class ValidationMixer:

    def validate_offset_value(self, offset: int):
        if offset < 0:
            raise InvalidOffsetException(offset)

    def validate_limit_value(self, limit: int):
        if limit <= 0:
            raise InvalidLimitException(limit)

    def validate_user(self, user_id: int):
        is_user_valid = self.user_storage.is_valid_user(user_id=user_id)
        is_not_valid_user = not is_user_valid
        if is_not_valid_user:
            raise InvalidUserException(user_id)

    
    def validate_admin(self, user_id: int):
        is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            raise UnAuthorizedUserException(user_id)


    def validate_resource(self, resource_id: int):
        is_valid_resource = self.resource_storage.is_valid_resource_id(
            resource_id=resource_id
        )
        is_not_valid_resource = not is_valid_resource
        if is_not_valid_resource:
            raise InvalidResourceIdException(resource_id)
