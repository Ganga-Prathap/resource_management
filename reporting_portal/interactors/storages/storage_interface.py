from abc import abstractmethod
from typing import Optional, List
from datetime import datetime
from reporting_portal.dtos.dtos import MealDto, ItemDto

class StorageInterface:

    @abstractmethod
    def validate_meal_id(self, meal_id: int) -> Optional[MealDto]:
        pass

    @abstractmethod
    def is_user_register_for_meal(self, user_id: int, meal_id: int) -> bool:
        pass

    @abstractmethod
    def update_user_meal_details(self, user_id: int,
                                 meal_id: int, item_dto_list: ItemDto):
        pass

    @abstractmethod
    def create_user_meal_details(self, user_id: int,
                                 meal_id: int, item_dto_list: ItemDto):
        pass
