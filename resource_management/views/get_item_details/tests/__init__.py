# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_item_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "items/{item_id}/details/v1/"

from .test_case_01 import TestCase01GetItemDetailsAPITestCase

__all__ = [
    "TestCase01GetItemDetailsAPITestCase"
]
