# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_resource_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/resources/{resource_id}/details/v1/"

from .test_case_01 import TestCase01GetResourceDetailsAPITestCase

__all__ = [
    "TestCase01GetResourceDetailsAPITestCase"
]
