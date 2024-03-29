import datetime
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.enums import AccessLevelEnum


def test_get_admin_requests_response(request_dto):

    #Arrange
    total_requests = 1

    expected_request_dict = {
            'total_requests': 1,
            'requests': 
        [
            {
                'request_id': 1,
                'username': 'Prathap',
                'profile_pic': 'https://prathap.profile',
                'resource_name': 'github',
                'item_name': 'item1',
                'access_level': AccessLevelEnum.READ.value,
                'due_date_time': datetime.datetime(2020, 6, 1, 0, 0)
            }
        ]
    }

    presenter = PresenterImplementation()

    #Act
    actual_request_dict = presenter.get_admin_requests_response(
        requests_dto=request_dto,
        total_requests=total_requests
    )

    assert actual_request_dict == expected_request_dict
