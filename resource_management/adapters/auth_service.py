from resource_management.dtos.dtos import UserDto

class AuthService:

    @property
    def interface(self):
        from resource_management_auth.interfaces.service_interface import \
            ServiceInterface
        return ServiceInterface()

    def user_login(self, username: str, password: str):
        return self.interface.user_login(
            username=username,
            password=password
        )

    def user_signup(self, username: str, password: str):
        return self.interface.user_signup(
            username=username,
            password=password
        )

    def get_user_details(self, user_id: int):
        user_dto = self.interface.get_user_dto(user_id=user_id)
        return UserDto(
            user_id=user_dto.user_id,
            username=user_dto.username,
            is_admin=user_dto.is_admin
            )
