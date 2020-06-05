from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.dtos.dtos import UserDto


def test_get_user_details_response(user_dto):

    #Arrange
    user_dto_dict = {
        'user_id': 1,
        'username': 'Prathap',
        'email': 'prathap@gmail.com',
        'job_role': 'backend_developer',
        'department': 'Technical',
        'gender': 'Male',
        'profile_pic': 'https://prathap.profile'
    }

    presenter = PresenterImplementation()

    #Act
    response = presenter.get_user_details_response(
        user_dto=user_dto
    )

    #Assert
    assert response == user_dto_dict
