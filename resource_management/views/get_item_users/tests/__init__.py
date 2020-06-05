# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_item_users"
REQUEST_METHOD = "get"
URL_SUFFIX = "items/{item_id}/users/v1/"

from .test_case_01 import TestCase01GetItemUsersAPITestCase

__all__ = [
    "TestCase01GetItemUsersAPITestCase"
]
