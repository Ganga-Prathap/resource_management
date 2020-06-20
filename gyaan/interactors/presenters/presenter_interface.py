from abc import abstractmethod
from typing import List
from gyaan.exceptions.exceptions import (
    InvalidDomainIdException,
    DomainUnfollowedUserException
)
from gyaan.dtos.dtos import (
    DomainDetailsDto,
    PostsDetailsDto,
    DomainWithPostsDto
)


class PresenterInterface:

    @abstractmethod
    def raise_exception_for_invalid_domain_id(
            self,
            error: InvalidDomainIdException):
        pass

    @abstractmethod
    def raise_exception_for_domain_unfollowed_user_exception(
            self,
            error: DomainUnfollowedUserException):
        pass

    @abstractmethod
    def get_domain_details_response(self, domain_details_dto: DomainDetailsDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_post_ids(self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_posts_response(self, post_details_dto: PostsDetailsDto):
        pass

    @abstractmethod
    def get_domain_posts_details_response(
            self, domain_posts_details: PostsDetailsDto):
        pass

    @abstractmethod
    def get_domain_with_posts_response(
            self,
            domain_with_posts: DomainWithPostsDto):
        pass
