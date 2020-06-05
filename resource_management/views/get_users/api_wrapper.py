from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_users_interactor import \
    GetUsersInteractor
from .validator_class import ValidatorClass
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id
    offset = kwargs['request_query_params']['offset']
    limit = kwargs['request_query_params']['limit']

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    users_dict = interactor.get_users(
        user_id=user_id,
        offset=offset,
        limit=limit
    )

    data = json.dumps(users_dict)
    response = HttpResponse(data, status=200)
    return response
