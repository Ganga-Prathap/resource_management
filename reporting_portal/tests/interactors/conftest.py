import pytest
import datetime
from typing import List
from reporting_portal.dtos.dtos import (
    ItemDto,
    MealDetailsDto,
    MealDto
)


@pytest.fixture()
def duplication_items_dto():
    items_dto = [
        ItemDto(
            item_id=1,
            item_quantity=2
        ),
        ItemDto(
            item_id=2,
            item_quantity=3
        ),
        ItemDto(
            item_id=3,
            item_quantity=2
        ),
        ItemDto(
            item_id=3,
            item_quantity=3
        )
    ]
    return items_dto

@pytest.fixture()
def meal_details_dto(duplication_items_dto):
    meals_dto = MealDetailsDto(
        user_id=1,
        meal_id=1,
        items_list = duplication_items_dto
    )
    return meals_dto

@pytest.fixture()
def invalid_item_quantity_dto():
    items_dto = [
        ItemDto(
            item_id=1,
            item_quantity=-1
        ),
        ItemDto(
            item_id=2,
            item_quantity=3
        ),
        ItemDto(
            item_id=3,
            item_quantity=2
        )
    ]
    return items_dto

@pytest.fixture()
def meal_details_dto2(invalid_item_quantity_dto):
    meals_dto = MealDetailsDto(
        user_id=1,
        meal_id=1,
        items_list = invalid_item_quantity_dto
    )
    return meals_dto


@pytest.fixture()
def meal_dto():
    meal_dto = MealDto(
        meal_id=1,
        meal_type='Break Fast',
        date_time=datetime.datetime(2020, 6, 1, 0, 0),
        item_ids=[1, 2]
    )
    return meal_dto

@pytest.fixture()
def meal_dto2():
    meal_dto = MealDto(
        meal_id=1,
        meal_type='Break Fast',
        date_time=datetime.datetime(2020, 6, 20, 0, 0),
        item_ids=[1, 2, 3]
    )
    return meal_dto

@pytest.fixture()
def meal_dto3():
    meal_dto = MealDto(
        meal_id=1,
        meal_type='Break Fast',
        date_time=datetime.datetime(2020, 6, 20, 0, 0),
        item_ids=[1, 2, 4]
    )
    return meal_dto
