from resource_management.dtos.dtos import UserDto

class AuthService:

    @property
    def interface(self):
        from resource_management_auth.interfaces.service_interface import \
            ServiceInterface
        return ServiceInterface()

    def get_user_details(self, user_id: int):
        user_dto = self.interface.get_user_dto(user_id=user_id)
        return UserDto(
            user_id=user_dto.user_id,
            username=user_dto.username,
            is_admin=user_dto.is_admin
            )
