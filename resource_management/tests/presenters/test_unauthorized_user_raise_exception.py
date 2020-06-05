import pytest
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.constants.exception_message import \
    UNAUTHORIZED_USER


def test_unauthorized_user_raise_exception():

    #Arrange
    exception_message = UNAUTHORIZED_USER[0]
    exception_response_status = UNAUTHORIZED_USER[1]

    presenter = PresenterImplementation()

    #Act
    with pytest.raises(BadRequest) as exception:
        presenter.unauthorized_user()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_response_status
