from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.exceptions.exceptions import (
    InvalidDomainIdException,
    DomainUnfollowedUserException
)


class DomainPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def domain_posts_wrapper(self, domain_id: int, user_id: int,
                             offset: int, limit: int,
                             presenter: PresenterInterface):
        try:
            return self.domain_posts_response(
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

    def domain_posts_response(self,
                              domain_id: int,
                              user_id: int,
                              offset: int,
                              limit: int,
                              presenter: PresenterInterface):
        domain_complete_posts_details_dto = self.domain_posts(
            domain_id=domain_id,
            user_id=user_id,
            offset=offset,
            limit=limit
        )
        response = presenter.get_domain_posts_details_response(
            domain_posts_details=domain_complete_posts_details_dto
        )
        return response

    def domain_posts(self, domain_id: int, user_id: int,
                     offset: int, limit: int):
        #TODO: validate domain_id
        is_domain_valid = self.storage.validate_domain_id(domain_id=domain_id)
        is_not_valid_domain = not is_domain_valid
        if is_not_valid_domain:
            raise InvalidDomainIdException(domain_id)

        #TODO: validate user_following domain or not
        domain_followed_user = self.storage.is_user_following_domain(
            domain_id=domain_id,
            user_id=user_id
        )
        domain_unfollowed_user = not domain_followed_user
        if domain_unfollowed_user:
            raise DomainUnfollowedUserException(user_id)

        #TODO: GET DOMAIN POST IDS
        post_ids = self.storage.get_domain_post_ids(
            domain_id=domain_id,
            offset=offset,
            limit=limit)

        #TODO: GET DOMAIN POSTS DETAILS
        get_posts_interactor = GetPostsInteractor(storage=self.storage)
        response = get_posts_interactor.get_posts(post_ids)
        return response
