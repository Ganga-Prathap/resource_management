import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_message import \
    INVALID_LIMIT


def test_invalid_offset_value_raise_exception():

    #Arrange
    exception_message = INVALID_LIMIT[0]
    exception_response_status = INVALID_LIMIT[1]
    presenter = PresenterImplementation()

    #Act
    with pytest.raises(BadRequest) as exception:
        presenter.invalidLimitValue()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_response_status
