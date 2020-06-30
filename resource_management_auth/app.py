from django.apps import AppConfig


class ResourceManagementAuthAppConfig(AppConfig):
    name = "resource_management_auth"

    def ready(self):
        from resource_management_auth import signals # pylint: disable=unused-variable
