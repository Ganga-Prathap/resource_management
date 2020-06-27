"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from resource_management.factories.factories import ResourceFactory


REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"resource_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase03DeleteResourceAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase03DeleteResourceAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.foo_user.is_admin = True
        self.foo_user.save()
        ResourceFactory.create()

    def test_case(self):
        self.default_test_case()
