from abc import abstractmethod
from typing import List
from .dtos import ResourceDto


class ResourceStorageInterface:

    @abstractmethod
    def create_resource(self, resource_name: str,
                         description: str,
                         link: str,
                         thumbnail: str) -> ResourceDto:
        pass

    @abstractmethod
    def is_valid_resource_id(self, resource_id: int) -> bool:
        pass

    @abstractmethod
    def get_resource_details(self, resource_id: int) -> ResourceDto:
        pass




    @abstractmethod
    def update_resource(self, resource_id: int,
                         resource_name: str,
                         description: str,
                         link: str,
                         thumbnail: str) -> ResourceDto:
        pass

    @abstractmethod
    def delete_resource(self, resource_id: int):
        pass

    @abstractmethod
    def get_admin_resources(self, offset: int, limit: int) -> List[ResourceDto]:
        pass

    @abstractmethod
    def get_total_resources_count(self) -> int:
        pass
