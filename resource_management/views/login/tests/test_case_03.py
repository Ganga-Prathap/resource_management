"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from resource_management.custom_test_utils.custom_test_utils import \
    CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "Prathap",
    "password": "12345"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}
import datetime
from unittest.mock import patch
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO

given_tokens = \
    UserAuthTokensDTO(
        user_id=1,
        access_token='rMeGKBv7qe64IounsrgMXXKbVkrN5U',
        refresh_token='s0lsy47ybxjQfmelr22Sp03DOuqzhg',
        expires_in=datetime.datetime(2023, 7, 28, 20, 10, 14, 724033)
    )


class TestCase03LoginAPITestCase(CustomTestUtils):

    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super().setupUser(
            username=username, password=password
        )
        
    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens',
              return_value=given_tokens)
    def test_case(self, auth_mock):
        from resource_management.factories.factories import UserFactory
        UserFactory.create(username='Prathap', password='12345')
        self.default_test_case()
