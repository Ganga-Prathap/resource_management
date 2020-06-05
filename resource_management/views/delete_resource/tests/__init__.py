# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "delete_resource"
REQUEST_METHOD = "delete"
URL_SUFFIX = "admin/resources/{resource_id}/delete/v1/"

from .test_case_01 import TestCase01DeleteResourceAPITestCase

__all__ = [
    "TestCase01DeleteResourceAPITestCase"
]
