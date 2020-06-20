import pytest
from unittest.mock import create_autospec
from reporting_portal.interactors.user_meal_quantity import \
    UserMealQuantityInteractor
from reporting_portal.interactors.storages.storage_interface import \
    StorageInterface
from reporting_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from reporting_portal.exceptions.exceptions import (
    InvalidMealIdException,
    ItemIdsDuplicationException,
    InvalidItemIdsException,
    InvalidItemQuantityException
)
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)


def test_invalid_meal_id_raise_exception(
        duplication_items_dto, meal_details_dto):

    #Arrange
    #user_id = meal_details_dto.user_id
    meal_id = meal_details_dto.meal_id
    #item_ids = meal_details_dto.items_list

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UserMealQuantityInteractor(storage=storage)
    storage.validate_meal_id.side_effect = InvalidMealIdException(meal_id)
    presenter.raise_exception_for_invalid_meal_id.side_effect = \
        NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.user_meal_quantity_wrapper(
            meal_details=meal_details_dto,
            presenter=presenter
        )

    #Assert
    storage.validate_meal_id.assert_called_with(meal_id=meal_id)
    presenter.raise_exception_for_invalid_meal_id.assert_called_once()


def test_invalid_registration_raise_time_out_exception(
        duplication_items_dto, meal_details_dto, meal_dto):

    #Arrange
    meal_id = meal_details_dto.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UserMealQuantityInteractor(storage=storage)
    storage.validate_meal_id.return_value = meal_dto
    presenter.raise_exception_for_time_out.side_effect = BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.user_meal_quantity_wrapper(
            meal_details=meal_details_dto,
            presenter=presenter
        )

    #Assert
    storage.validate_meal_id.assert_called_with(meal_id=meal_id)
    presenter.raise_exception_for_time_out.assert_called_once()



def test_duplication_of_item_ids_raise_exception(
        meal_details_dto, meal_dto2):

    #Arrange
    meal_id = meal_details_dto.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UserMealQuantityInteractor(storage=storage)
    storage.validate_meal_id.return_value = meal_dto2
    presenter.raise_exception_for_duplication_in_item_ids.side_effect = \
        BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.user_meal_quantity_wrapper(
            meal_details=meal_details_dto,
            presenter=presenter
        )

    #Assert
    storage.validate_meal_id.assert_called_with(meal_id=meal_id)
    presenter.raise_exception_for_duplication_in_item_ids.assert_called_once()
    call_obj = presenter.raise_exception_for_duplication_in_item_ids.call_args
    error_object = call_obj.args[0]
    assert error_object.duplicate_item_ids == [3]


def test_invalid_item_ids_raise_exception(
        meal_details_dto2, meal_dto3):

    #Arrange
    meal_id = meal_details_dto2.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UserMealQuantityInteractor(storage=storage)
    storage.validate_meal_id.return_value = meal_dto3
    presenter.raise_exception_for_invalid_item_ids.side_effect = \
        NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.user_meal_quantity_wrapper(
            meal_details=meal_details_dto2,
            presenter=presenter
        )

    #Assert
    storage.validate_meal_id.assert_called_with(meal_id=meal_id)
    presenter.raise_exception_for_invalid_item_ids.assert_called_once()
    call_obj = presenter.raise_exception_for_invalid_item_ids.call_args
    error_object = call_obj.args[0]
    assert error_object.invalid_item_ids == [3]


def test_invalid_item_quantity_raise_exception(
        meal_details_dto2, meal_dto2):

    #Arrange
    meal_id = meal_details_dto2.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = UserMealQuantityInteractor(storage=storage)
    storage.validate_meal_id.return_value = meal_dto2
    presenter.raise_exception_for_invalid_item_quantity.side_effect = \
        InvalidItemQuantityException

    #Act
    with pytest.raises(InvalidItemQuantityException):
        interactor.user_meal_quantity_wrapper(
            meal_details=meal_details_dto2,
            presenter=presenter
        )

    #Assert
    storage.validate_meal_id.assert_called_with(meal_id=meal_id)
    presenter.raise_exception_for_invalid_item_quantity.assert_called_once()

