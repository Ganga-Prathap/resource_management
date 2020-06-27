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
    "password": "12345wq"
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


class TestCase02LoginAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super().setupUser(
            username=username, password=password
        )
        print("*"*50)
        print("1: \n")
        print("user: \n", self.foo_user.username)
        print("password: \n", self.foo_user.password)

    def test_case(self):
        from resource_management.factories.factories import UserFactory
        UserFactory.create(username='Prathap', password='12345')
        self.default_test_case()
        print("3: \n")
