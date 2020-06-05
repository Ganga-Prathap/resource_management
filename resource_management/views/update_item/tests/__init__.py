# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "update_item"
REQUEST_METHOD = "post"
URL_SUFFIX = "items/{item_id}/update/v1/"

from .test_case_01 import TestCase01UpdateItemAPITestCase

__all__ = [
    "TestCase01UpdateItemAPITestCase"
]
