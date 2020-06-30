import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management_auth.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management_auth.constants.exception_message import \
    INVALID_PASSWORD



def test_invalid_password_raise_exception():

    #Arrange
    exception_message = INVALID_PASSWORD[0]
    exception_response_status = INVALID_PASSWORD[1]
    presenter = PresenterImplementation()

    #Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_invalid_password()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_response_status
