from abc import abstractmethod
from typing import List
from .dtos import ItemDto


class ItemStorageInterface:

    @abstractmethod
    def create_item(self, resource_id: int,
                    title: str,
                    description: str,
                    link: str) -> ItemDto:
        pass

    @abstractmethod
    def get_resource_items(self, resource_id: int,
                           offset: int, limit: int) -> List[ItemDto]:
        pass

    @abstractmethod
    def get_resource_items_count(self, resource_id: int) -> int:
        pass

    @abstractmethod
    def is_valid_item_id(self, item_id: int) -> bool:
        pass

    @abstractmethod
    def get_item_details(self, item_id: int) -> ItemDto:
        pass

    @abstractmethod
    def update_item(self, item_id: int,
                    title: str,
                    description: str,
                    link: str) -> ItemDto:
        pass

    @abstractmethod
    def delete_items(self, item_ids: List[int]):
        pass

    @abstractmethod
    def get_user_items(self, user_id: int,
                       offset: int, limit: int) -> List[ItemDto]:
        pass

    @abstractmethod
    def get_user_items_count(self, user_id: int) -> int:
        pass
