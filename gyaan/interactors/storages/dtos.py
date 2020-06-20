from typing import List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class DomainDto:
    domain_id: int
    domain_name: str
    description: str

@dataclass
class DomainStatsDto:
    domain_id: int
    followers_count: int
    posts_count: int
    bookmarked_count: int

@dataclass
class UserDetailsDto:
    user_id: int
    username: str
    profile_pic: str

@dataclass
class DomainJoinRequestDto:
    request_id: int
    user_id: int

@dataclass
class PostDto:
    post_id: int
    title: str
    content: str
    posted_at: datetime
    posted_by: int

@dataclass
class TagDto:
    tag_id: int
    name: str


@dataclass
class PostTagDto:
    post_id: int
    tag_id: int


@dataclass
class PostTagDetailsDto:
    tags: List[TagDto]
    post_tag_ids: List[PostTagDto]

@dataclass
class PostReactionsCountDto:
    post_id: int
    reactions_count: int

@dataclass
class PostCommentsCountDto:
    post_id: int
    comments_count: int

@dataclass
class CommentReactionsCountDto:
    comment_id: int
    reactions_count: int

@dataclass
class CommentRepliesCountDto:
    comment_id: int
    replies_count: int

@dataclass
class CommentDto:
    comment_id: int
    content: str
    commented_at: datetime
    commented_by: int
