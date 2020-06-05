from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_admin_requests_interactor import \
    GetAdminRequestsInteractor
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
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
    request_storage = RequestStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetAdminRequestsInteractor(
        user_storage=user_storage,
        request_storage=request_storage,
        presenter=presenter
    )

    requests_dict = interactor.get_admin_requests(
        user_id=user_id,
        offset=offset,
        limit=limit
    )
    data = json.dumps(requests_dict)
    response = HttpResponse(data, status=200)
    return response
