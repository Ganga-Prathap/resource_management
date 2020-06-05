from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.dtos.dtos import ItemDto

def test_get_user_items_response(item_dto):

    #Arrange
    items_count = 1
    items_dto = [item_dto]
    expected_items_dict = {
        "total_items": 1,
        "items": [{
            'item_id': 1,
            'title': 'item1',
            'resource_name': 'github',
            'description': 'item_description',
            'link': 'https://item1'
        }]
    }

    presenter = PresenterImplementation()

    #Act
    actual_items_dict = presenter.get_user_items_response(
        items_dto=items_dto,
        items_count=items_count
    )

    #Assert
    assert actual_items_dict == expected_items_dict
