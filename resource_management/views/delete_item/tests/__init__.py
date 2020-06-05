# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "delete_item"
REQUEST_METHOD = "delete"
URL_SUFFIX = "items/delete/v1/"

from .test_case_01 import TestCase01DeleteItemAPITestCase

__all__ = [
    "TestCase01DeleteItemAPITestCase"
]
