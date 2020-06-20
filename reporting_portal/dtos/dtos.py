from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class ItemDto:
    item_id: int
    item_quantity: int

@dataclass
class MealDetailsDto:
    user_id: int
    meal_id: int
    items_list: List[ItemDto]

@dataclass
class MealDto:
    meal_id: int
    meal_type: str
    date_time: datetime
    item_ids: List[int]
