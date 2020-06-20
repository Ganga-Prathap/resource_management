from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.exceptions.exceptions import (
    InvalidDomainIdException,
    DomainUnfollowedUserException
)
from gyaan.dtos.dtos import DomainDetailsDto


class DomainDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def domain_details_wrapper(self,
                               domain_id: int,
                               user_id: int,
                               presenter: PresenterInterface):
        try:
            return self.domain_details_response(
                domain_id=domain_id,
                user_id=user_id,
                presenter=presenter
            )
        except InvalidDomainIdException as error:
            presenter.raise_exception_for_invalid_domain_id(error)
        except DomainUnfollowedUserException as error:
            presenter.raise_exception_for_domain_unfollowed_user_exception(
                    error)

    def domain_details_response(self, domain_id: int,
                                user_id: int, presenter=PresenterInterface):
            domain_details_dto = self.domain_details(
                domain_id=domain_id,
                user_id=user_id
            )
            return presenter.get_domain_details_response(domain_details_dto)


    def domain_details(self, domain_id: int, user_id: int):

        #TODO: validate domain
        domain_dto = self.storage.get_domain_dto(domain_id=domain_id)

        #TODO: check user following domain or not
        domain_followed_user = self.storage.is_user_following_domain(
            domain_id=domain_id,
            user_id=user_id
        )
        domain_unfollowed_user = not domain_followed_user
        if domain_unfollowed_user:
            raise DomainUnfollowedUserException(user_id)

        #TODO: Domain stats
        domain_stats = self.storage.get_domain_stats(domain_id)

        #TODO: Domain experts
        domain_expert_ids = self.storage.get_domain_expert_ids(domain_id)
        domain_experts_details = self.storage.get_users_details(
                domain_expert_ids)

        #TODO: Domain request details
        is_user_domain_expert, domain_requests_dtos, requested_users_dtos = \
            self._get_domain_request_details(
                user_id=user_id,
                domain_id=domain_id
            )

        response = DomainDetailsDto(
            domain=domain_dto,
            domain_stats=domain_stats,
            domain_experts=domain_experts_details,
            is_user_domain_expert=is_user_domain_expert,
            join_requests=domain_requests_dtos,
            requested_users=requested_users_dtos
        )
        return response


    def _get_domain_request_details(self, user_id: int, domain_id: int):
        domain_join_requests_dtos = []
        requested_users_dtos = []
        is_user_domain_expert = self.storage.is_user_domain_expert(
            domain_id=domain_id,
            user_id=user_id
        )

        if is_user_domain_expert:
            domain_join_requests_dtos = self.storage.get_domain_join_requests(
                domain_id=domain_id
            )

        if domain_join_requests_dtos:
            requested_users_dtos = self.storage.get_users_details(
                user_ids=[
                    dto.user_id for dto in domain_join_requests_dtos
                ]
            )
        return is_user_domain_expert, domain_join_requests_dtos,\
            requested_users_dtos
