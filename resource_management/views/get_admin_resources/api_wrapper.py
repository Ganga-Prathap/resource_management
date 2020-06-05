from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_admin_resources_interactor import \
    GetAdminResourcesInteractor
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
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
    resource_storage = ResourceStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetAdminResourcesInteractor(
        user_storage=user_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    resource_dict_list = interactor.get_admin_resources(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    data = json.dumps(resource_dict_list)
    response = HttpResponse(data, status=200)
    return response
