# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "create_item"
REQUEST_METHOD = "post"
URL_SUFFIX = "resources/{resource_id}/item/create/v1/"

from .test_case_01 import TestCase01CreateItemAPITestCase
from .test_case_02 import TestCase02CreateItemAPITestCase
from .test_case_03 import TestCase03CreateItemAPITestCase

__all__ = [
    "TestCase01CreateItemAPITestCase",
    "TestCase02CreateItemAPITestCase",
    "TestCase03CreateItemAPITestCase"
]
