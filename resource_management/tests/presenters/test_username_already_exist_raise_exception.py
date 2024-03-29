import pytest
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.constants.exception_message import \
    USER_NAME_ALREADY_EXIST


def test_username_already_exist_raise_exception():

    #Arrange
    exception_message = USER_NAME_ALREADY_EXIST[0]
    exception_response_status = USER_NAME_ALREADY_EXIST[1]

    presenter = PresenterImplementation()

    #Act
    with pytest.raises(BadRequest) as exception:
        presenter.username_already_exists()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_response_status
