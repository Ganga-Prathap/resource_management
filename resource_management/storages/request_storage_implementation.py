from typing import List
from resource_management.interactors.storages.request_storage_interface import \
    RequestStorageInterface
from resource_management.models.request import Request
from resource_management.dtos.dtos import RequestDto

class RequestStorageImplementation(RequestStorageInterface):

    def _get_request_dto(self, request_obj):
        request_dto = RequestDto(
            request_id=request_obj.id,
            username=request_obj.user.username,
            profile_pic=request_obj.user.profile_pic,
            resource_name=request_obj.item.resource.resource_name,
            item_name=request_obj.item.title,
            access_level=request_obj.access_level,
            due_date_time=request_obj.due_date_time
        )
        return request_dto

    def get_admin_requests(self, offset: int, limit: int) -> List[RequestDto]:
        request_objs = Request.objects.select_related(
                              'item__resource', 'user').all()\
                              [offset:offset+limit]
        request_dtos_list = []
        for request_obj in request_objs:
            request_dto = self._get_request_dto(request_obj)
            request_dtos_list.append(request_dto)
        return request_dtos_list

    def get_total_requests_count(self) -> int:
        requests_count = Request.objects.count()
        return requests_count
