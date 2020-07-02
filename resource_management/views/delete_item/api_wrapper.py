from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.delete_items_interactor import \
    DeleteItemsInteractor
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id
    requested_data = kwargs['request_data']
    item_ids = requested_data['item_ids']

    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()

    interactor = DeleteItemsInteractor(
        item_storage=item_storage,
        presenter=presenter
    )


    interactor.delete_items(
        user_id=user_id,
        item_ids=item_ids
    )

    data = json.dumps({'response': 'deleted successfully'})
    return HttpResponse(data, status=200)
