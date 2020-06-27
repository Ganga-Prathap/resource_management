# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "delete_item"
REQUEST_METHOD = "post"
URL_SUFFIX = "items/delete/v1/"

from .test_case_01 import TestCase01DeleteItemAPITestCase
from .test_case_02 import TestCase02DeleteItemAPITestCase
from .test_case_03 import TestCase03DeleteItemAPITestCase

__all__ = [
    "TestCase01DeleteItemAPITestCase",
    "TestCase02DeleteItemAPITestCase",
    "TestCase03DeleteItemAPITestCase"
]
