from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.domain_details_interactor import DomainDetailsInteractor
from gyaan.interactors.domain_posts_interactor import DomainPostsInteractor
from gyaan.exceptions.exceptions import (
    InvalidDomainIdException,
    DomainUnfollowedUserException
)
from gyaan.dtos.dtos import DomainWithPostsDto


class DomainWithPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def domain_with_posts_wrapper(self, domain_id: int,
                                  user_id: int,
                                  offset: int,
                                  limit: int,
                                  presenter: PresenterInterface):
        try:
            return self.domain_with_posts_response(
                domain_id=domain_id,
                user_id=user_id,
                offset=offset,
                limit=limit,
                presenter=presenter
            )
        except InvalidDomainIdException as error:
            presenter.raise_exception_for_invalid_domain_id(error)
        except DomainUnfollowedUserException as error:
            presenter.raise_exception_for_domain_unfollowed_user_exception(
                error
            )

    def domain_with_posts_response(self, domain_id: int,
                                   user_id: int,
                                   offset: int,
                                   limit: int,
                                   presenter: PresenterInterface):
        domain_with_posts_dto = self.domain_with_posts(
            domain_id=domain_id,
            user_id=user_id,
            offset=offset,
            limit=limit
        )
        return presenter.get_domain_with_posts_response(domain_with_posts_dto)

    def domain_with_posts(self, domain_id: int,
                          user_id: int,
                          offset: int,
                          limit: int):
        domain_details_interactor = DomainDetailsInteractor(
            storage=self.storage
        )
        domain_details_dto = domain_details_interactor.domain_details(
            domain_id=domain_id,
            user_id=user_id
        )

        domain_posts_interactor = DomainPostsInteractor(
            storage=self.storage
        )
        domain_posts_details_dto = domain_posts_interactor.domain_posts(
            domain_id=domain_id,
            user_id=user_id,
            offset=offset,
            limit=limit
        )
        return DomainWithPostsDto(
            domain_details_dto=domain_details_dto,
            domain_posts_dto=domain_posts_details_dto
        )
