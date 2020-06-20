from abc import abstractmethod
from typing import List
from .dtos import (
    DomainDto,
    DomainStatsDto,
    UserDetailsDto,
    DomainJoinRequestDto,
    PostDto,
    PostTagDetailsDto,
    PostReactionsCountDto,
    PostCommentsCountDto,
    CommentReactionsCountDto,
    CommentRepliesCountDto,
    CommentDto
)

class StorageInterface:

    @abstractmethod
    def get_domain_dto(self, domain_id: int) -> DomainDto:
        pass

    @abstractmethod
    def is_user_following_domain(self, domain_id: int, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> DomainStatsDto:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_users_details(self, user_ids: List[int]) -> List[UserDetailsDto]:
        pass

    @abstractmethod
    def is_user_domain_expert(self, domain_id: int, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_join_requests(self, domain_id: int) -> \
            List[DomainJoinRequestDto]:
        pass

    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_post_details(self, post_ids: List[int]) -> List[PostDto]:
        pass

    @abstractmethod
    def get_post_tags_details(self, post_ids: List[int]) -> PostTagDetailsDto:
        pass

    @abstractmethod
    def get_post_reactions_count(self, post_ids: List[int]) -> \
            List[PostReactionsCountDto]:
        pass

    @abstractmethod
    def get_post_comments_count(self, post_ids: List[int]) -> \
            List[PostCommentsCountDto]:
        pass

    @abstractmethod
    def get_latest_comment_ids(self, post_id: int, count: int) -> List[int]:
        pass

    @abstractmethod
    def get_comment_reactions_count(self, comment_ids: List[int]) -> \
            List[CommentReactionsCountDto]:
        pass

    @abstractmethod
    def get_comment_replies_count(self, comment_ids: List[int]) -> \
            List[CommentRepliesCountDto]:
        pass

    @abstractmethod
    def get_comment_details(self, comment_ids: List[int]) -> List[CommentDto]:
        pass

    @abstractmethod
    def validate_domain_id(self, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_post_ids(self, domain_id: int,
                            offset: int, limit: int) -> List[int]:
        pass
