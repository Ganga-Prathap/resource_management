from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_item_details_interactor import \
    GetItemDetailsInteractor
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
    item_id = kwargs['item_id']

    user_storage = UserStorageImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetItemDetailsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    item_dict = interactor.get_item_details(
        user_id=user_id,
        item_id=item_id
    )

    data = json.dumps(item_dict)
    response = HttpResponse(data, status=200)
    return response
