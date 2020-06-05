from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.user_profile_update_interactor import \
    UserProfileUpdateInteractor
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
    username = requested_data['username']
    email = requested_data['email']
    job_role = requested_data['job_role']
    department = requested_data['department']
    gender = requested_data['gender']
    profile_pic = requested_data['profile_pic']

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = UserProfileUpdateInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    interactor.user_profile_update(
        user_id=user_id,
        username=username,
        email=email,
        job_role=job_role,
        department=department,
        gender=gender,
        profile_pic=profile_pic
    )

    data = json.dumps({'response': 'updated successfully'})
    response = HttpResponse(data, status=200)
    return response
