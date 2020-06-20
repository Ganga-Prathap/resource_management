from abc import abstractmethod
from reporting_portal.exceptions.exceptions import (
    InvalidMealIdException,
    ItemIdsDuplicationException,
    InvalidItemIdsException
)


class PresenterInterface:

    @abstractmethod
    def raise_exception_for_invalid_meal_id(
            self,
            InvalidMealIdException):
        pass

    @abstractmethod
    def raise_exception_for_time_out(self):
        pass

    @abstractmethod
    def raise_exception_for_duplication_in_item_ids(
            self,
            error: ItemIdsDuplicationException):
        pass

    @abstractmethod
    def raise_exception_for_invalid_item_ids(
            self,
            error: InvalidItemIdsException):
        pass

    @abstractmethod
    def raise_exception_for_invalid_item_quantity(self):
        pass
