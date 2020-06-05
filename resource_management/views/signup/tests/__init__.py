# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "signup"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/signup/v1/"

from .test_case_01 import TestCase01SignupAPITestCase

__all__ = [
    "TestCase01SignupAPITestCase"
]
