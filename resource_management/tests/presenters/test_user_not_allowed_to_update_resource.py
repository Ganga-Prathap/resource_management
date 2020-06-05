import pytest
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import BadRequest
from resource_management.constants.exception_message import \
    USER_NOT_ALLOWED_TO_UPDATE


def test_user_not_allowed_to_update_exception():

    #Arrange
    exception_message = USER_NOT_ALLOWED_TO_UPDATE[0]
    exception_response_status = USER_NOT_ALLOWED_TO_UPDATE[1]

    presenter = PresenterImplementation()

    #Act
    with pytest.raises(BadRequest) as exception:
        presenter.user_not_allowed_to_update_resource()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_response_status
