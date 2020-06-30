import factory, factory.django
from resource_management_auth.models.user import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "username-%d" % n)
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_admin = factory.Iterator([True, False])
