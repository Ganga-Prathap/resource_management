from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.dtos.dtos import ItemDto


def update_item_response():

    #Arrange
    item_dto = ItemDto(
        item_id=1,
        title='item1.0',
        resource_name='github',
        description='item_description1.0',
        link='https://item1.0'
    )

    expected_item_dict = {
        'item_id': 1,
        'title': 'item1.0',
        'resource_name': 'github',
        'description': 'item_description1.0',
        'link': 'https://item1.0'
    }

    presenter = PresenterImplementation()

    #Act
    item_dict = presenter.update_item_response(
        item_dto=item_dto
    )

    #Assert
    assert item_dict == expected_item_dict
