# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_admin_resources"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/resources/v1/"

from .test_case_01 import TestCase01GetAdminResourcesAPITestCase
from .test_case_02 import TestCase02GetAdminResourcesAPITestCase

__all__ = [
    "TestCase01GetAdminResourcesAPITestCase",
    "TestCase02GetAdminResourcesAPITestCase"
]
