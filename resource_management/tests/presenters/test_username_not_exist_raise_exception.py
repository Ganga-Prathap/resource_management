import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_message import \
    USER_DOES_NOT_EXISTS


def test_username_not_exist_raise_exception():

    #Arrange
    exception_message = USER_DOES_NOT_EXISTS[0]
    exception_response_status = USER_DOES_NOT_EXISTS[1]
    presenter = PresenterImplementation()

    #Act
    with pytest.raises(NotFound) as exception:
        presenter.username_not_exists()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_response_status
