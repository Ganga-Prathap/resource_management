import pytest
from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation

@pytest.mark.django_db
def test_get_total_requests_count(create_resource,
                                  create_item,
                                  create_request):
    #Assert
    total_requests_count = 1

    request_storage = RequestStorageImplementation()

    #Act
    actual_requests_count = request_storage.get_total_requests_count()

    #Assert
    assert actual_requests_count == total_requests_count
