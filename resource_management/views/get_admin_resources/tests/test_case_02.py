"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from resource_management.custom_test_utils.custom_test_utils import \
    CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX




REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {"offset": 0, "limit": 2},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02GetAdminResourcesAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super().setupUser(
            username=username, password=password
        )
        self.foo_user.is_admin = True
        self.foo_user.save()

        self.resources_of_admin()

    def test_case(self):
        self.default_test_case()
