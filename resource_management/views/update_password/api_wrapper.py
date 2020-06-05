from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.update_password_interactor import \
    UpdatePasswordInteractor
from resource_management.storages.user_storage_implementation import \
    UserStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id = user.id
    requested_data = kwargs['request_data']
    password = requested_data['password']

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = UpdatePasswordInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    interactor.update_password(
        user_id=user_id,
        password=password
    )
    data = json.dumps({"response": "deleted successfully"})
    response = HttpResponse(data, status=200)
    return response
