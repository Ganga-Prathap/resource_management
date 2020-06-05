# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_admin_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/requests/v1/"

from .test_case_01 import TestCase01GetAdminRequestsAPITestCase

__all__ = [
    "TestCase01GetAdminRequestsAPITestCase"
]
