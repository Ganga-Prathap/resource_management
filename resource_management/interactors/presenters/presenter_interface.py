from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from resource_management.interactors.storages.dtos import (
    ResourceDto,
    UserDto,
    ItemDto,
    RequestDto
)


class PresenterInterface:

    @abstractmethod
    def username_not_exists(self):
        pass

    @abstractmethod
    def invalid_password(self):
        pass

    @abstractmethod
    def get_tokens_service(self, token: UserAuthTokensDTO,
                           is_admin: bool):
        pass

    @abstractmethod
    def username_already_exists(self):
        pass

    @abstractmethod
    def invalid_user(self):
        pass

    @abstractmethod
    def get_user_details_response(self, user_dto: UserDto):
        pass

    @abstractmethod
    def user_not_allowed_to_create_resource(self):
        pass

    @abstractmethod
    def unauthorized_user(self):
        print("143:\n")
        pass

    @abstractmethod
    def invalid_resource_id(self):
        pass

    @abstractmethod
    def get_resource_details_response(self, resourcedto: ResourceDto):
        pass

    @abstractmethod
    def user_not_allowed_to_update_resource(self):
        pass

    @abstractmethod
    def get_admin_resources_response(self,
                                     resources_list_dto: List[ResourceDto],
                                     resources_count: int):
        pass

    @abstractmethod
    def invalidOffsetValue(self):
        pass

    @abstractmethod
    def invalidLimitValue(self):
        pass

    @abstractmethod
    def get_resource_items_response(self, items_dto_list: List[ItemDto],
                                    items_count: int):
        pass

    @abstractmethod
    def invalid_item_id(self):
        pass

    @abstractmethod
    def get_item_details_response(self, item_dto: ItemDto):
        pass

    @abstractmethod
    def get_item_users_response(self, users_dto: List[UserDto]):
        pass

    @abstractmethod
    def get_admin_requests_response(self, requests_dto: List[RequestDto],
                                   total_requests: int):
        pass

    @abstractmethod
    def get_users_response(self, users_dto: List[UserDto],
                           users_count: int):
        pass

    @abstractmethod
    def get_user_items_response(self, items_dto: List[ItemDto],
                                items_count: int):
        pass
