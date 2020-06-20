import pytest
from datetime import datetime
from gyaan.dtos.dtos import (
    DomainDto,
    DomainStatsDto,
    UserDetailsDto,
    DomainJoinRequestDto,
    PostDto,
    TagDto,
    PostTagDto,
    PostTagDetailsDto,
    PostReactionsCountDto,
    PostCommentsCountDto,
    CommentReactionsCountDto,
    CommentRepliesCountDto
)

@pytest.fixture
def domain_dto():
    domaindto = DomainDto(
        domain_id=1,
        domain_name='django',
        description='django is one of the webframe work'
    )
    return domaindto

@pytest.fixture
def domain_stats():
    domainstats = DomainStatsDto(
        domain_id=1,
        followers_count=4,
        posts_count=5,
        bookmarked_count=2
    )
    return domainstats

@pytest.fixture
def domain_experts_dto():
    userdto = [UserDetailsDto(
        user_id=2,
        username='naveen',
        profile_pic='https://naveen.com/pic'
    )]
    return userdto

@pytest.fixture
def domain_join_requests_dtos():
    requests_dtos = [
        DomainJoinRequestDto(
            request_id=1,
            user_id=3
        )
    ]
    return requests_dtos

@pytest.fixture
def domain_requests_users_dto():
    request_users = [
        UserDetailsDto(
            user_id=3,
            username='daya',
            profile_pic='https://daya.com/pic'
        )
    ]
    return request_users

@pytest.fixture
def posts_dto():
    postdto = [
        PostDto(
            post_id=1,
            title='post1',
            content='post1 content',
            posted_at=datetime(2020, 6, 18, 0, 0),
            posted_by=1
        ),
        PostDto(
            post_id=2,
            title='post2',
            content='post2 content',
            posted_at=datetime(2020, 6, 17, 0, 0),
            posted_by=1
        )
    ]
    return postdto

@pytest.fixture
def tags_dto():
    tagdto = [
        TagDto(
            tag_id=1,
            name='tag1'
        )
    ]
    return tagdto

@pytest.fixture
def post_tags_dto():
    posttagdto = [
        PostTagDto(
            post_id=1,
            tag_id=1
        )
    ]
    return posttagdto

@pytest.fixture
def post_tags_details_dto(tags_dto, post_tags_dto):
    post_tag_details = [
        PostTagDetailsDto(
            tags=tags_dto,
            post_tag_ids=post_tags_dto
        )
    ]
    return post_tag_details

@pytest.fixture
def post_reaction_count_dto():
    post_reactionsdto = [
        PostReactionsCountDto(
            post_id=1,
            reactions_count=2
        )
    ]
    return post_reactionsdto

@pytest.fixture
def post_comments_count_dto():
    post_commentsdto = [
        PostCommentsCountDto(
            post_id=1,
            comments_count=2
        )
    ]
    return post_commentsdto
