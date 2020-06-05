from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.dtos.dtos import ResourceDto


def test_get_admin_resources_responses(admin_resources_dto):

    #Arrange
    resources_count = 1
    resource_dto_list = admin_resources_dto
    expected_resources_dict = {
        "total_resources": 1,
        "resources": [{
            "resource_id": 1,
            "resource_name": 'github',
            "description": 'it has repository',
            "link": 'https://github.com',
            "thumbnail": 'https://github'
        }]
    }

    presenter = PresenterImplementation()

    #Act
    actual_dict = presenter.get_admin_resources_response(
        resources_list_dto=resource_dto_list,
        resources_count=resources_count
    )

    #Assert
    assert actual_dict == expected_resources_dict
