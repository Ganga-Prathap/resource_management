from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.dtos.dtos import ItemDto


def test_get_item_details_response(item_dto):

    #Arrange

    expected_item_dict = {
        'item_id': 1,
        'title': 'item1',
        'resource_name': 'github',
        'description': 'item_description',
        'link': 'https://item1'
    }

    presenter = PresenterImplementation()

    #Act
    actual_item_dict = presenter.get_item_details_response(
        item_dto=item_dto
    )

    #Assert
    assert actual_item_dict == expected_item_dict
