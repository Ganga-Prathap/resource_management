from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.create_item_interactor import \
    CreateItemInteractor
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id
    resource_id = kwargs['resource_id']
    requested_data = kwargs['request_data']
    title = requested_data['title']
    description = requested_data['description']
    link = requested_data['link']

    resource_storage = ResourceStorageImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()

    interactor = CreateItemInteractor(
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    interactor.create_item(
        user_id=user_id,
        resource_id=resource_id,
        title=title,
        description=description,
        link=link
    )
    data = json.dumps({"response": "created successfully"})
    response = HttpResponse(data, status=201)
    return response
