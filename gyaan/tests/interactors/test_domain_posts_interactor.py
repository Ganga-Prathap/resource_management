import pytest
from unittest.mock import create_autospec, patch
from gyaan.interactors.domain_posts_interactor import DomainPostsInteractor
from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.get_posts_interactor import \
    GetPostsInteractor
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)


def test_invalid_domain_id_raise_exception():

    #Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainPostsInteractor(storage=storage)
    storage.validate_domain_id.return_value = False
    presenter.raise_exception_for_invalid_domain_id.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.domain_posts_wrapper(
            domain_id=domain_id,
            user_id=user_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Act
    storage.validate_domain_id.assert_called_with(domain_id=domain_id)
    presenter.raise_exception_for_invalid_domain_id.assert_called_once()
    call_obj = presenter.raise_exception_for_invalid_domain_id.call_args
    error_obj = call_obj.args[0]
    assert error_obj.domain_id == domain_id

def test_domain_unfollowed_user_raise_exception():

    #Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainPostsInteractor(storage=storage)
    storage.is_user_following_domain.return_value = False
    presenter.raise_exception_for_domain_unfollowed_user_exception.side_effect \
            = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.domain_posts_wrapper(
            domain_id=domain_id,
            user_id=user_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    #Assert
    storage.validate_domain_id.assert_called_with(domain_id=domain_id)
    presenter.raise_exception_for_domain_unfollowed_user_exception.assert_called_once()
    call_obj = \
        presenter.raise_exception_for_domain_unfollowed_user_exception.call_args
    error_obj = call_obj.args[0]
    assert error_obj.user_id == user_id


@patch.object(GetPostsInteractor, 'get_posts')
def test_get_domain_posts_details(get_post_mock, post_details_dto):

    #Arrange
    get_post_mock.return_value = post_details_dto
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 1
    post_ids = [1]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_domain_post_ids.return_value = post_ids

    interactor = DomainPostsInteractor(storage=storage)

    #Act
    interactor.domain_posts_wrapper(
        domain_id=domain_id,
        user_id=user_id,
        offset=offset,
        limit=limit,
        presenter=presenter
    )

    #Assert
    storage.validate_domain_id.assert_called_with(domain_id=domain_id)
    storage.is_user_following_domain.assert_called_with(
        domain_id=domain_id,
        user_id=user_id
    )
    storage.get_domain_post_ids.assert_called_with(
        domain_id=domain_id,
        offset=offset,
        limit=limit
    )
    presenter.get_domain_posts_details_response.assert_called_once_with(
        domain_posts_details=post_details_dto
    )
