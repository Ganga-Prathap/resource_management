"""
# TODO: Update test case description
"""
from unittest.mock import patch
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


class TestCase02DeleteResourceAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02DeleteResourceAPITestCase, self).setupUser(
            username=username, password=password
        )
        ResourceFactory.create()

    @patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')
    def test_case(self, get_user_dto_mock):
        from resource_management.dtos.dtos import UserDto
        userdto = UserDto(
            user_id=1,
            username='Nav',
            is_admin=False
        )
        get_user_dto_mock.return_value = userdto
        self.default_test_case()
