from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass
from resource_management_auth.interactors.login_interactor import \
    LoginInteractor
from resource_management_auth.storages.storage_implementation import \
    StorageImplementation
from resource_management_auth.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    
    requested_data = kwargs['request_data']
    username = requested_data['username']
    password = requested_data['password']

    storage = StorageImplementation()
    oauth2_storage = OAuth2SQLStorage()
    presenter = PresenterImplementation()

    interactor = LoginInteractor(
        storage=storage,
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
