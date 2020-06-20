from reporting_portal.interactors.user_meal_quantity import \
    UserMealQuantity
from reporting_portal.interactors.storages.storage_interface import \
    StorageInterface
from reporting_portal.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_invalid_mail_id_raise_exception(items_dto, meal_details_dto):

    #Arrange
    user_id = meal_details_dto.user_id
    meal_id = meal_details_dto.meal_id
