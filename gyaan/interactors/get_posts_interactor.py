from typing import List
from gyaan.interactors.storages.storage_interface import \
    StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.exceptions.exceptions import InvalidPostidsException
from gyaan.dtos.dtos import PostsDetailsDto


class GetPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_posts_wrapper(self, post_ids: List[int],
                          presenter: PresenterInterface):
        try:
            return self._get_posts_response(
                post_ids=post_ids,
                presenter=presenter
            )
        except InvalidPostidsException as error:
            presenter.raise_exception_for_invalid_post_ids(error)

    def _get_posts_response(self, post_ids: List[int],
                            presenter: PresenterInterface):
        posts_details_dto = self.get_posts(post_ids=post_ids)
        response = presenter.get_posts_response(posts_details_dto)
        return response

    def get_posts(self, post_ids: List[int]):
        unique_post_ids = self._get_unique_post_ids(post_ids)
        self._validate_post_ids(unique_post_ids)

        posts_dto = self.storage.get_post_details(unique_post_ids)
        posts_tag_dto = self.storage.get_post_tags_details(unique_post_ids)
        posts_reactions_count = self.storage.get_post_reactions_count(
            unique_post_ids
        )
        posts_comments_count = self.storage.get_post_comments_count(
            unique_post_ids
        )

        comment_ids = self._get_latest_comment_ids(unique_post_ids)
        comments_reactions_count = self.storage.get_comment_reactions_count(
            comment_ids
        )
        comments_replies_count = self.storage.get_comment_replies_count(
            comment_ids
        )
        comments_dto = self.storage.get_comment_details(comment_ids)

        user_ids = [post_dto.posted_by for post_dto in posts_dto]
        user_ids += [
            comment_dto.commented_by for comment_dto in comments_dto
        ]
        user_ids = list(set(user_ids))
        users_dto = self.storage.get_users_details(user_ids=user_ids)

        return PostsDetailsDto(
            posts_dtos=posts_dto,
            posts_reactions_count=posts_reactions_count,
            posts_comments_count=posts_comments_count,
            comments_reactions_count=comments_reactions_count,
            comments_replies_count=comments_replies_count,
            comments_dto=comments_dto,
            post_tag_ids=posts_tag_dto.post_tag_ids,
            tags=posts_tag_dto.tags,
            users_dto=users_dto
        )

    def _get_latest_comment_ids(self, post_ids):
        comment_ids = []
        for post_id in post_ids:
            comment_ids += self.storage.get_latest_comment_ids(
                post_id=post_id, count=1)
        return comment_ids

    def _validate_post_ids(self, unique_post_ids):
        valid_post_ids = self.storage.get_valid_post_ids(unique_post_ids)
        invalid_post_ids = [
            post_id
            for post_id in unique_post_ids
            if post_id not in valid_post_ids
        ]
        if invalid_post_ids:
            raise InvalidPostidsException(invalid_post_ids)

    def _get_unique_post_ids(self, post_ids):
        return list(set(post_ids))
