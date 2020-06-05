from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_user_details_interactor import \
    GetUserDetailsInteractor
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetUserDetailsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )
    user_dict = interactor.get_user_details(
        user_id=user_id
    )
    data = json.dumps(user_dict)
    response = HttpResponse(data, status=200)
    return response
