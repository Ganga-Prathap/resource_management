import datetime
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from common.dtos import UserAuthTokensDTO


def test_get_token_service():

    #Arrange
    is_admin = False
    user_auth_token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token='rMeGKBv7qe64IounsrgMXXKbVkrN5U',
        refresh_token='s0lsy47ybxjQfmelr22Sp03DOuqzhg',
        expires_in=datetime.datetime(2023, 7, 28, 20, 10, 14, 724033)
    )
    expected_access_token = {
        'access_token': 'rMeGKBv7qe64IounsrgMXXKbVkrN5U',
        'is_admin': is_admin
    }

    presenter = PresenterImplementation()

    #Act
    access_token = presenter.get_tokens_service(
        token=user_auth_token_dto,
        is_admin=is_admin
    )

    #Assert
    assert access_token == expected_access_token
