import pytest
from django_swagger_utils.utils.test import CustomAPITestCase
from resource_management.factories.factories import (
    UserFactory,
    ResourceFactory,
    ItemFactory,
    RequestFactory
)
from freezegun import freeze_time


class CustomTestUtils(CustomAPITestCase):

    def setupUser(self, username, password):
        super(CustomTestUtils, self).setupUser(
            username=username, password=password
        )
        ResourceFactory.reset_sequence()
        ItemFactory.reset_sequence()
        RequestFactory.reset_sequence()

    @freeze_time('2020-06-26')
    def requests_of_users_fixture(self):

        users = UserFactory.create_batch(2)
        resource = ResourceFactory.create()

        item = ItemFactory.create(resource=resource)
        requests = []
        requests.extend(RequestFactory.create_batch(
            1, user=users[0], item=item)
        )
        requests.extend(RequestFactory.create_batch(
            1, user=users[1], item=item)
        )

    def resources_of_admin(self):

        ResourceFactory.create_batch(3)

    def items_of_resource(self):

        resource = ResourceFactory.create()
        ItemFactory.create_batch(2, resource=resource)

    def get_user_items(self, user):

        resources = ResourceFactory.create_batch(3)
        ItemFactory.create(resource=resources[0], users=[user])
        ItemFactory.create(resource=resources[1], users=[user])
        ItemFactory.create(resource=resources[2], users=[user])
