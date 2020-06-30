import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management_auth.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management_auth.constants.exception_message import \
    INVALID_USER


def test_invalid_user_raise_exception():

    #Arrange
    exception_message = INVALID_USER[0]
    exception_response_status = INVALID_USER[1]
    presenter = PresenterImplementation()

    #Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_exception_for_invalid_user_id()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_response_status
