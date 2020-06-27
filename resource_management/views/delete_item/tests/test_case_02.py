"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from resource_management.factories.factories import (
    ResourceFactory,
    ItemFactory
)


REQUEST_BODY = """
{
    "item_ids": [
        2
    ]
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02DeleteItemAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02DeleteItemAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.foo_user.is_admin = True
        self.foo_user.save()
        resource = ResourceFactory.create()
        ItemFactory.create(resource=resource)

    def test_case(self):
        self.default_test_case()