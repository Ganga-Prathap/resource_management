import pytest
from unittest.mock import create_autospec
from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)
from gyaan.dtos.dtos import PostsDetailsDto


def test_get_posts_with_invalid_post_ids_raise_exception():

    #Arrange
    post_ids = [1, 2, 3, 4]
    valid_post_ids = [1, 2, 3]
    invalid_ids = [4]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetPostsInteractor(storage=storage)
    storage.get_valid_post_ids.return_value = valid_post_ids
    presenter.raise_exception_for_invalid_post_ids.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.get_posts_wrapper(
            post_ids=post_ids,
            presenter=presenter
        )

    #Assert
    storage.get_valid_post_ids.assert_called_with(post_ids=post_ids)
    presenter.raise_exception_for_invalid_post_ids.assert_called_once()
    call_obj = presenter.raise_exception_for_invalid_post_ids.call_args
    error_obj = call_obj.args[0]
    assert error_obj.post_ids == invalid_ids


def test_get_posts_details(posts_dto,
                           post_tags_details_dto,
                           post_reaction_count_dto,
                           post_comments_count_dto,
                           comment_reaction_count_dto,
                           comment_replies_count_dto,
                           comments_dto,
                           users_dto):

    #Arrange
    post_ids = [1]
    comment_ids = [1, 2]
    user_ids = [1, 2]

    post_details_dto = PostsDetailsDto(
        posts_dtos=posts_dto,
        posts_reactions_count=post_reaction_count_dto,
        posts_comments_count=post_comments_count_dto,
        comments_reactions_count=comment_reaction_count_dto,
        comments_replies_count=comment_replies_count_dto,
        comments_dto=comments_dto,
        post_tag_ids=post_tags_details_dto.post_tag_ids,
        tags=post_tags_details_dto.tags,
        users_dto=users_dto  
    )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetPostsInteractor(storage=storage)
    storage.get_valid_post_ids.return_value = post_ids
    storage.get_post_details.return_value = posts_dto
    storage.get_post_tags_details.return_value = post_tags_details_dto
    storage.get_post_reactions_count.return_value = post_reaction_count_dto
    storage.get_post_comments_count.return_value = post_comments_count_dto
    storage.get_latest_comment_ids.return_value = comment_ids
    storage.get_comment_reactions_count.return_value = \
        comment_reaction_count_dto
    storage.get_comment_replies_count.return_value = comment_replies_count_dto
    storage.get_comment_details.return_value = comments_dto
    storage.get_users_details.return_value = users_dto

    #Act
    interactor.get_posts_wrapper(
        post_ids=post_ids,
        presenter=presenter
    )

    #Assert
    storage.get_valid_post_ids.assert_called_with(post_ids=post_ids)
    storage.get_post_details.assert_called_with(post_ids=post_ids)
    storage.get_post_tags_details.assert_called_with(post_ids=post_ids)
    storage.get_post_reactions_count.assert_called_with(post_ids=post_ids)
    storage.get_post_comments_count.assert_called_with(post_ids=post_ids)
    storage.get_latest_comment_ids.assert_called_with(
        post_id=post_ids[0],
        count=1)
    storage.get_comment_reactions_count.assert_called_with(
        comment_ids=comment_ids
    )
    storage.get_comment_replies_count.assert_called_with(
        comment_ids=comment_ids
    )
    storage.get_comment_details.assert_called_with(comment_ids)
    storage.get_users_details.assert_called_with(user_ids=user_ids)
    presenter.get_posts_response.assert_called_once_with(post_details_dto)
