from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.login_interactor import \
    LoginInteractor
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    requested_data = kwargs['request_data']
    username = requested_data['username']
    password = requested_data['password']

    user_storage = UserStorageImplementation()
    oauth2_storage = OAuth2SQLStorage()
    presenter = PresenterImplementation()

    interactor = LoginInteractor(
        user_storage=user_storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )

    access_token = interactor.login(
        username=username,
        password=password
    )

    data = json.dumps(access_token)
    response = HttpResponse(data, status=200)
    return response
