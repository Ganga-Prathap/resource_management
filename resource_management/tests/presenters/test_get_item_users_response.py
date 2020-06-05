from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_item_users_response(user_dto):

    #Arrange
    users_dto = [user_dto]

    expected_users_dict = [{
        'user_id': 1,
        'username': 'Prathap',
        'email': 'prathap@gmail.com',
        'job_role': 'backend_developer',
        'department': 'Technical',
        'gender': 'Male',
        'profile_pic': 'https://prathap.profile'
    }]

    presenter = PresenterImplementation()

    #Act
    actula_users_dict = presenter.get_item_users_response(
        users_dto=users_dto
    )

    #Assert
    assert actula_users_dict == expected_users_dict
