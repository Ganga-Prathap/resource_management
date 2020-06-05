from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.dtos.dtos import ResourceDto


def test_get_admin_resources_responses():

    #Arrange
    resource_dto = ResourceDto(
        resource_id=1,
        resource_name='github',
        description='it has repository',
        link='https://github.com',
        thumbnail='https://github'
    )
    expected_dict_list = {
        "resource_id": 1,
        "resource_name": 'github',
        "description": 'it has repository',
        "link": 'https://github.com',
        'thumbnail': 'https://github'
    }

    presenter = PresenterImplementation()

    #Act
    response = presenter.get_resource_details_response(
        resourcedto=resource_dto
    )

    #Assert
    assert response == expected_dict_list
