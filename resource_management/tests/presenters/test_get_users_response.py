from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_users_response(user_dto):

    #Arrange
    users_count = 1
    users_dto = [user_dto]

    expected_users_dict = {
        "total_users": 1,
        "users": [{
            'user_id': 1,
            'username': 'Prathap',
            'email': 'prathap@gmail.com',
            'job_role': 'backend_developer',
            'department': 'Technical',
            'gender': 'Male',
            'profile_pic': 'https://prathap.profile'
        }]
    }

    presenter = PresenterImplementation()

    #Act
    actual_users_dict = presenter.get_users_response(
        users_dto=users_dto,
        users_count=users_count
    )

    #Assert
    assert actual_users_dict == expected_users_dict
