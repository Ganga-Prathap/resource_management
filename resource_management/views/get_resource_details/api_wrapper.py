from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_resource_details_interactor import \
    GetResourceDetailsInteractor
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print("\n\n",123,"\n\n")
    user = kwargs['user']
    user_id = user.id
    resource_id = kwargs['resource_id']
    print("\n\nresource_id: ", resource_id, "\n\n")

    user_storage = UserStorageImplementation()
    resource_storage = ResourceStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetResourceDetailsInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    resource_dict = interactor.get_resource_details(
        user_id=user_id,
        resource_id=resource_id
    )

    data = json.dumps(resource_dict)
    response = HttpResponse(data, status=200)
    return response
