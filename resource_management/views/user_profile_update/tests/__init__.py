# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "user_profile_update"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/profile/update/v1/"

from .test_case_01 import TestCase01UserProfileUpdateAPITestCase

__all__ = [
    "TestCase01UserProfileUpdateAPITestCase"
]
