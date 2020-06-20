import pytest
from unittest.mock import create_autospec, call
from gyaan.interactors.domain_details_interactor import DomainDetailsInteractor
from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.exceptions.exceptions import (
    InvalidDomainIdException,
    DomainUnfollowedUserException
)
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)
from gyaan.dtos.dtos import DomainDetailsDto


def test_invalid_domain_id_raise_exception():

    #Arrange
    invalid_domain_id = 1
    user_id = 1
    invalid_domain_exception = InvalidDomainIdException(invalid_domain_id)

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsInteractor(storage=storage)
    storage.get_domain_dto.side_effect = invalid_domain_exception
    presenter.raise_exception_for_invalid_domain_id.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.domain_details_wrapper(
            domain_id=invalid_domain_id,
            user_id=user_id,
            presenter=presenter
        )

    #Assert
    storage.get_domain_dto.assert_called_with(domain_id=invalid_domain_id)
    presenter.raise_exception_for_invalid_domain_id.assert_called_once_with(
        invalid_domain_exception
    )


def test_domain_unfollowed_user_raise_exception():

    #Arrange
    domain_id = 1
    user_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = DomainDetailsInteractor(storage=storage)
    storage.is_user_following_domain.return_value = False
    presenter.raise_exception_for_domain_unfollowed_user_exception.side_effect \
            = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.domain_details_wrapper(
            domain_id=domain_id,
            user_id=user_id,
            presenter=presenter
        )

    #Assert
    storage.get_domain_dto.assert_called_with(domain_id=domain_id)
    presenter.raise_exception_for_domain_unfollowed_user_exception.assert_called_once()
    call_obj = presenter.raise_exception_for_domain_unfollowed_user_exception.call_args
    error_obj = call_obj.args[0]
    assert error_obj.user_id == user_id


def test_get_domain_details_when_user_is_domain_expert(
                                                    domain_dto,
                                                    domain_stats,
                                                    domain_experts_dto,
                                                    domain_join_requests_dtos,
                                                    domain_requests_users_dto):

    #Arrange
    user_id = 1
    domain_id = 1
    expert_ids = [2]
    requested_users_ids = [3]

    expected_domain_details_dto = DomainDetailsDto(
        domain=domain_dto,
        domain_stats=domain_stats,
        domain_experts=domain_experts_dto,
        is_user_domain_expert=True,
        join_requests=domain_join_requests_dtos,
        requested_users=domain_requests_users_dto
    )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_domain_dto.return_value = domain_dto
    storage.is_user_following_domain.return_value = True
    storage.get_domain_stats.return_value = domain_stats
    storage.get_domain_expert_ids.return_value = expert_ids
    storage.get_users_details.side_effect = [
            domain_experts_dto, domain_requests_users_dto]
    storage.is_user_domain_expert.return_value = True
    storage.get_domain_join_requests.return_value = domain_join_requests_dtos

    interactor = DomainDetailsInteractor(storage=storage)

    #Act
    interactor.domain_details_wrapper(
        domain_id=domain_id,
        user_id=user_id,
        presenter=presenter
    )

    #Assert
    storage.get_domain_dto.assert_called_with(domain_id=domain_id)
    storage.get_domain_stats.assert_called_with(domain_id=domain_id)
    storage.get_domain_expert_ids.assert_called_with(domain_id=domain_id)
    storage.get_users_details.assert_has_calls([call(expert_ids),
        call(requested_users_ids)]
    )
    storage.is_user_domain_expert.assert_called_with(
        domain_id=domain_id,
        user_id=user_id
    )
    storage.get_domain_join_requests.assert_called_with(domain_id=domain_id)
    presenter.get_domain_details_response.assert_called_once_with(
        expected_domain_details_dto)


def test_get_domain_details_with_user(domain_dto,
                                      domain_stats,
                                      domain_experts_dto,
                                      ):

    #Arrange
    user_id = 1
    domain_id = 1
    expert_ids = [2]

    expected_domain_details_dto = DomainDetailsDto(
        domain=domain_dto,
        domain_stats=domain_stats,
        domain_experts=domain_experts_dto,
        is_user_domain_expert=False,
        join_requests=[],
        requested_users=[]
    )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_domain_dto.return_value = domain_dto
    storage.is_user_following_domain.return_value = True
    storage.get_domain_stats.return_value = domain_stats
    storage.get_domain_expert_ids.return_value = expert_ids
    storage.get_users_details.side_effect = [domain_experts_dto]
    storage.is_user_domain_expert.return_value = False

    interactor = DomainDetailsInteractor(storage=storage)

    #Act
    interactor.domain_details_wrapper(
        domain_id=domain_id,
        user_id=user_id,
        presenter=presenter
    )

    #Assert
    storage.get_domain_dto.assert_called_with(domain_id=domain_id)
    storage.get_domain_stats.assert_called_with(domain_id=domain_id)
    storage.get_domain_expert_ids.assert_called_with(domain_id=domain_id)
    storage.get_users_details.assert_called_with(expert_ids)
    storage.is_user_domain_expert.assert_called_with(
        domain_id=domain_id,
        user_id=user_id
    )
    presenter.get_domain_details_response.assert_called_once_with(
        expected_domain_details_dto)
