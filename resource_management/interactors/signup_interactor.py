from resource_management.interactors.storages.user_storage_interface import \
    UserStorageInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.oauth2_storage import OAuth2SQLStorage


class SignupInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 oauth2_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.oauth2_storage = oauth2_storage
        self.presenter = presenter

    def signup(self, username: str, password: str):
        self.check_username_validity(username)

        user_id = self.user_storage.signup_new_user(
            username=username,
            password=password
        )
        from common.oauth_user_auth_tokens_service import \
            OAuthUserAuthTokensService
        token_service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2_storage
        )
        is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)
        token = token_service.create_user_auth_tokens(
            user_id=user_id
        )
        response = self.presenter.get_tokens_service(
            token=token,
            is_admin=is_admin
        )
        return response

    def check_username_validity(self, username: str):
        is_username_exists = self.user_storage.validate_username(
            username=username)
        if is_username_exists:
            response = self.presenter.username_already_exists()
            return response
