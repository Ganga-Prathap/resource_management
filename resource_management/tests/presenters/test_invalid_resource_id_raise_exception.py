import pytest
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from django_swagger_utils.drf_server.exceptions import NotFound
from resource_management.constants.exception_message import \
    INVALID_RESOURCE


def test_invalid_resource_id_raise_exception():

    #Arrange
    exception_message = INVALID_RESOURCE[0]
    exception_response_status = INVALID_RESOURCE[1]

    presenter = PresenterImplementation()

    #Act
    with pytest.raises(NotFound) as exception:
        presenter.invalid_resource_id()

    #Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_response_status
