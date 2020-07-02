from typing import List
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.dtos import UserAuthTokensDTO
from resource_management.dtos.dtos import (
    UserDto,
    ResourceDto,
    ItemDto,
    RequestDto
)
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)
from resource_management.constants.exception_message import (
    USER_DOES_NOT_EXISTS,
    INVALID_PASSWORD,
    USER_NAME_ALREADY_EXIST,
    INVALID_USER,
    UNAUTHORIZED_USER,
    USER_NOT_ALLOWED_TO_CREATE,
    USER_NOT_ALLOWED_TO_UPDATE,
    INVALID_RESOURCE,
    INVALID_ITEM,
    INVALID_OFFSET,
    INVALID_LIMIT
)


class PresenterImplementation(PresenterInterface):

    def username_not_exists(self):
        raise NotFound(*USER_DOES_NOT_EXISTS)

    def invalid_password(self):
        raise BadRequest(*INVALID_PASSWORD)


    def get_tokens_service(self, token: UserAuthTokensDTO,
                           is_admin: bool):
        return {
            'access_token': token.access_token,
            'is_admin': is_admin
        }

    def username_already_exists(self):
        raise BadRequest(*USER_NAME_ALREADY_EXIST)

    def invalid_user(self):
        raise BadRequest(*INVALID_USER)

    @staticmethod
    def _get_user_dict(user_dto):
        user_dict = {
            'user_id': user_dto.user_id,
            'username': user_dto.username,
            'email': user_dto.email,
            'department': user_dto.department,
            'job_role': user_dto.job_role,
            'gender': user_dto.gender,
            'profile_pic': user_dto.profile_pic
        }
        return user_dict

    def get_user_details_response(self, user_dto: UserDto):
        return self._get_user_dict(user_dto)

    def user_not_allowed_to_create_resource(self):
        raise BadRequest(*USER_NOT_ALLOWED_TO_CREATE)

    def unauthorized_user(self):
        raise BadRequest(*UNAUTHORIZED_USER)

    def invalid_resource_id(self):
        raise NotFound(*INVALID_RESOURCE)

    @staticmethod
    def _get_resource_dict_form(resourcedto):
        resourcedto_dict = {
            "resource_id": resourcedto.resource_id,
            "resource_name": resourcedto.resource_name,
            "description": resourcedto.description,
            "link": resourcedto.link,
            "thumbnail": resourcedto.thumbnail
        }
        return resourcedto_dict

    def get_resource_details_response(self, resourcedto: ResourceDto):
        return self._get_resource_dict_form(resourcedto)

    def user_not_allowed_to_update_resource(self):
        raise BadRequest(*USER_NOT_ALLOWED_TO_UPDATE)

    def get_admin_resources_response(self,
                                     resources_list_dto: List[ResourceDto],
                                     resources_count: int):
        resource_list = []
        for resourcedto in resources_list_dto:
            resource_dict = self._get_resource_dict_form(resourcedto)
            resource_list.append(resource_dict)
        resources = {
            'total_resources': resources_count,
            'resources': resource_list
        }
        return resources

    def invalidOffsetValue(self):
        raise BadRequest(*INVALID_OFFSET)

    def invalidLimitValue(self):
        raise BadRequest(*INVALID_LIMIT)

    @staticmethod
    def _get_item_dict(item_dto):
        item_dict = {
            'item_id': item_dto.item_id,
            'title': item_dto.title,
            'resource_name': item_dto.resource_name,
            'description': item_dto.description,
            'link': item_dto.link
        }
        return item_dict

    def get_resource_items_response(self, items_dto_list: List[ItemDto],
                                    items_count: int):
        items_dict_list = []
        for item_dto in items_dto_list:
            item_dict = self._get_item_dict(item_dto)
            items_dict_list.append(item_dict)

        items = {
            "total_items": items_count,
            "items": items_dict_list
        }
        return items

    def invalid_item_id(self):
        raise NotFound(*INVALID_ITEM)

    def get_item_details_response(self, item_dto: ItemDto):
        return self._get_item_dict(item_dto)

    def get_item_users_response(self, users_dto: List[UserDto]):
        users_dict_list = []
        for user_dto in users_dto:
            user_dict = self._get_user_dict(user_dto)
            users_dict_list.append(user_dict)
        return users_dict_list

    @staticmethod
    def _get_request_dict(request_dto, user_dto):
        request_dict = {
            'request_id': request_dto.request_id,
            'username': user_dto.username,
            'resource_name': request_dto.resource_name,
            'item_name': request_dto.item_name,
            'access_level': request_dto.access_level,
            'due_date_time': request_dto.due_date_time
        }
        return request_dict

    def get_admin_requests_response(self, requests_dto: List[RequestDto],
                                   total_requests: int,
                                   users_dto: List[UserDto]):
        request_dict_list = []
        for request_dto in requests_dto:
            for user_dto in users_dto:
                if request_dto.user_id == user_dto.user_id:
                    request_dict = self._get_request_dict(request_dto, user_dto)
                    request_dict_list.append(request_dict)
        requests = {
            'total_requests': total_requests,
            'requests': request_dict_list
        }
        return requests

    def get_users_response(self, users_dto: List[UserDto],
                           users_count: int):
        users_dict_list = []
        for user_dto in users_dto:
            user_dict = self._get_user_dict(user_dto)
            users_dict_list.append(user_dict)
        users = {
            "total_users": users_count,
            "users": users_dict_list
        }
        return users

    def get_user_items_response(self, items_dto: List[ItemDto],
                                items_count: int):
        items_dict_list = []
        for item_dto in items_dto:
            item_dict = self._get_item_dict(item_dto)
            items_dict_list.append(item_dict)
        items = {
            "total_items": items_count,
            "items": items_dict_list
        }
        return items
