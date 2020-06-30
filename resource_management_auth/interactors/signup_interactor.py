from resource_management_auth.interactors.storages.storage_interface import \
    StorageInterface
from resource_management_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.oauth2_storage import OAuth2SQLStorage


class SignupInteractor:

    def __init__(self, storage: StorageInterface,
                 oauth2_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.storage = storage
        self.oauth2_storage = oauth2_storage
        self.presenter = presenter

    def signup(self, username: str, password: str):
        self.check_username_validity(username)

        user_id = self.storage.signup_new_user(
            username=username,
            password=password
        )

        from common.oauth_user_auth_tokens_service import \
            OAuthUserAuthTokensService
        token_service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2_storage
        )
        is_admin = self.storage.is_user_admin_or_not(user_id=user_id)
        token = token_service.create_user_auth_tokens(
            user_id=user_id
        )
        response = self.presenter.get_tokens_service(
            token=token,
            is_admin=is_admin
        )
        return response

    def check_username_validity(self, username: str):
        is_username_exists = self.storage.validate_username(
            username=username)
        if is_username_exists:
            response = self.presenter.raise_exception_for_username_already_exist()
            return response
