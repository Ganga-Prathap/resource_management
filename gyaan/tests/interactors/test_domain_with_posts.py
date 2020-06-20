import pytest
from unittest.mock import create_autospec, patch
from gyaan.interactors.domain_with_posts_interactor import \
    DomainWithPostsInteractor
from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.domain_details_interactor import DomainDetailsInteractor
from gyaan.interactors.domain_posts_interactor import DomainPostsInteractor
from gyaan.dtos.dtos import DomainWithPostsDto


@patch.object(DomainPostsInteractor, 'domain_posts')
@patch.object(DomainDetailsInteractor, 'domain_details')
def test_domain_with_posts(domain_details_mock, domain_posts_mock,
                           domain_details_dto, post_details_dto):
    #Arrange
    domain_details_mock.return_value = domain_details_dto
    domain_posts_mock.return_value = post_details_dto
    domain_with_posts = DomainWithPostsDto(
        domain_details_dto=domain_details_dto,
        domain_posts_dto=post_details_dto
    )

    domain_id = 1
    user_id = 1
    offset = 0
    limit = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainWithPostsInteractor(storage=storage)

    #Act
    interactor.domain_with_posts_wrapper(
        domain_id=domain_id,
        user_id=user_id,
        offset=offset,
        limit=limit,
        presenter=presenter
    )

    #Assert
    presenter.get_domain_with_posts_response(
        domain_with_posts=domain_with_posts
    )
