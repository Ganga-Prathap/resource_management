from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_user_items_interactor import \
    GetUserItemsInteractor
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id
    offset = kwargs['request_query_params']['offset']
    limit = kwargs['request_query_params']['limit']

    user_storage = UserStorageImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetUserItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    items_dict = interactor.get_user_items(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    data = json.dumps(items_dict)
    response = HttpResponse(data, status=200)
    return response
