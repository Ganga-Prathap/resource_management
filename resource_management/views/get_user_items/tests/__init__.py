# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_user_items"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/items/v1/"

from .test_case_01 import TestCase01GetUserItemsAPITestCase

__all__ = [
    "TestCase01GetUserItemsAPITestCase"
]
