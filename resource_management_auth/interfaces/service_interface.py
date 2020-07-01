from resource_management_auth.interactors.login_interactor import \
    LoginInteractor
from resource_management_auth.interactors.signup_interactor import \
    SignupInteractor
from resource_management_auth.interactors.get_user_details_interactor \
    import GetUserDetails
from resource_management_auth.storages.storage_implementation import \
    StorageImplementation
from resource_management_auth.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage


class ServiceInterface:

    @staticmethod
    def user_login(username: str, password: str):
        storage = StorageImplementation()
        oauth2_storage = OAuth2SQLStorage()
        presenter = PresenterImplementation()
        interactor = LoginInteractor(
            storage=storage,
            oauth2_storage=oauth2_storage,
            presenter=presenter
        )
        interactor.login(username=username, password=password)

    @staticmethod
    def user_signup(username: str, password: str):
        storage = StorageImplementation()
        oauth2_storage = OAuth2SQLStorage()
        presenter = PresenterImplementation()
        interactor = SignupInteractor(
            storage=storage,
            oauth2_storage=oauth2_storage,
            presenter=presenter
        )
        interactor.signup(username=username, password=password)

    @staticmethod
    def get_user_dto(user_id: int):
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        interactor = GetUserDetails(storage=storage, presenter=presenter)
        user_dto = interactor.get_user_details(user_id=user_id)
        return user_dto
