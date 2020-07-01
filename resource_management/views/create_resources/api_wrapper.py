from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.create_resource_interactor import \
    CreateResourcesInteractor
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id
    requested_data = kwargs['request_data']
    resource_name = requested_data['resource_name']
    description = requested_data['description']
    link = requested_data['link']
    thumbnail = requested_data['thumbnail']

    resource_storage = ResourceStorageImplementation()
    presenter = PresenterImplementation()

    interactor = CreateResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    interactor.create_resource(
        user_id=user_id,
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )

    data = json.dumps({"response": "created successfully"})
    response = HttpResponse(data, status=201)
    return response
