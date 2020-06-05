from typing import List
from resource_management.interactors.storages.resource_storage_interface import \
    ResourceStorageInterface
from resource_management.models.resource import Resource
from resource_management.dtos.dtos import ResourceDto


class ResourceStorageImplementation:

    def _get_resource_dto(self, resource_obj):
        resource_dto = ResourceDto(
            resource_id=resource_obj.id,
            resource_name=resource_obj.resource_name,
            description=resource_obj.description,
            link=resource_obj.link,
            thumbnail=resource_obj.thumbnail
        )
        return resource_dto

    def create_resource(self, resource_name: str,
                         description: str,
                         link: str,
                         thumbnail: str) -> ResourceDto:

        Resource.objects.create(
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )

    def is_valid_resource_id(self, resource_id: int) -> bool:
        response = Resource.objects.filter(id=resource_id).exists()
        return response

    def get_resource_details(self, resource_id: int) -> ResourceDto:
        resource_obj = Resource.objects.get(id=resource_id)
        resource_dto = self._get_resource_dto(resource_obj)
        return resource_dto

    def update_resource(self, resource_id: int,
                         resource_name: str,
                         description: str,
                         link: str,
                         thumbnail: str) -> ResourceDto:
        Resource.objects.filter(id=resource_id).update(
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )
        resource_obj = Resource.objects.get(id=resource_id)
        resource_dto = self._get_resource_dto(resource_obj)
        return resource_dto

    def delete_resource(self, resource_id: int):
        Resource.objects.get(id=resource_id).delete()

    def get_admin_resources(self, offset: int,
                            limit: int) -> List[ResourceDto]:
        resources_list = []
        resource_objs = Resource.objects.all()[offset:offset+limit]
        for resource_obj in resource_objs:
            resource_dto = self._get_resource_dto(resource_obj)
            resources_list.append(resource_dto)
        return resources_list

    def get_total_resources_count(self) -> int:
        resources_count = Resource.objects.count()
        return resources_count
