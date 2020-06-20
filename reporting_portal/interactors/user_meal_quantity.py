from datetime import datetime, timedelta
from typing import List
from reporting_portal.dtos.dtos import (
    ItemDto,
    MealDetailsDto,
    MealDto
)
from reporting_portal.interactors.storages.storage_interface import \
    StorageInterface
from reporting_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from reporting_portal.exceptions.exceptions import (
    InvalidMealIdException,
    TimeOutException,
    ItemIdsDuplicationException,
    InvalidItemIdsException,
    InvalidItemQuantityException
)


class UserMealQuantityInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def user_meal_quantity_wrapper(self,
                                   meal_details: MealDetailsDto,
                                   presenter: PresenterInterface):
        try:
            self.user_meal_quantity(meal_details=meal_details)
        except InvalidMealIdException as error:
            presenter.raise_exception_for_invalid_meal_id(error)
        except TimeOutException:
            presenter.raise_exception_for_time_out()
        except ItemIdsDuplicationException as error:
            presenter.raise_exception_for_duplication_in_item_ids(error)
        except InvalidItemIdsException as error:
            presenter.raise_exception_for_invalid_item_ids(error)
        except InvalidItemQuantityException:
            presenter.raise_exception_for_invalid_item_quantity()

    def user_meal_quantity(self,
                           meal_details: MealDetailsDto):
        user_id = meal_details.user_id
        meal_id = meal_details.meal_id
        items_list = meal_details.items_list

        item_ids, item_quantities = self._get_item_ids_and_item_quntities(
            items_list
        )

        #TODO: validate_meal_id
        meal_dto = self.storage.validate_meal_id(meal_id=meal_id)
        print("1:")
        #TODO: validate_date_time
        meal_datetime = meal_dto.date_time
        present_datetime = datetime.now()
        remove_two_hours_in_meal_datetime = meal_datetime - timedelta(hours=2)
        invalid_registration = present_datetime > \
            remove_two_hours_in_meal_datetime
        if invalid_registration:
            raise TimeOutException
        print("2:")
        #TODO: check item_ids_duplication
        ids_count = len(meal_dto.item_ids)

        
        is_duplication_in_ids = not(ids_count == len(item_ids))
        #duplicate_item_ids = [3]
        if is_duplication_in_ids:
            duplicate_item_ids = self._get_duplicate_item_ids(
                meal_item_ids=meal_dto.item_ids, duplicate_item_ids=item_ids)
            raise ItemIdsDuplicationException(duplicate_item_ids)
        print("3")
        #TODO: validate item_ids
        invalid_item_ids = self._validate_item_ids(meal_dto.item_ids, item_ids)
        if len(invalid_item_ids) > 0:
            raise InvalidItemIdsException(invalid_item_ids)
        #TODO: check item_ids_quantity
        self._validate_item_quantities(item_quantities)
        #TODO: check is user register for meal or not
        is_user_register = self.storage.is_user_register_for_meal(
            user_id=user_id,
            meal_id=meal_id
        )
        #TODO: if yes update meal for user
        item_dto_list = self._get_item_dto_list(items_list)
        if is_user_register:
            self.storage.update_user_meal_details(
                user_id=user_id,
                meal_id=meal_id,
                item_dto_list=item_dto_list
                )
        #TODO: otherwise register meal for user
        else:
            self.storage.create_user_meal_details(
                user_id=user_id,
                meal_id=meal_id,
                item_dto_list=item_dto_list
            )


    def _get_item_dto_list(self, items_list):
        item_dto_list = []
        for item in items_list:
            item_dto = ItemDto(
                item_id=item.item_id,
                item_quantity=item.item_quantity
            )
            item_dto_list.append(item_dto)
        return item_dto_list

    @staticmethod
    def _validate_item_ids(meal_item_ids, validate_item_ids):
        invalid_ids = []
        for item_id in validate_item_ids:
            if item_id not in meal_item_ids:
                invalid_ids.append(item_id)
        return invalid_ids

    @staticmethod
    def _get_item_ids_and_item_quntities(items_list):
        item_ids = []
        item_quantities = []
        for item in items_list:
            item_ids.append(item.item_id)
            item_quantities.append(item.item_quantity)
        return item_ids, item_quantities

    @staticmethod
    def _validate_item_quantities(item_quantities):
        for item_quantity in item_quantities:
            if item_quantity < 0:
                raise InvalidItemQuantityException

    @staticmethod
    def _get_duplicate_item_ids(meal_item_ids, duplicate_item_ids):
        duplicate_ids = []
        for meal_item_id in meal_item_ids:
            count = duplicate_item_ids.count(meal_item_id)
            if count > 1 and meal_item_id not in duplicate_ids:
                duplicate_ids.append(meal_item_id)
        return duplicate_ids
