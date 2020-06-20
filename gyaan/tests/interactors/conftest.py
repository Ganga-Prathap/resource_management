import pytest
import datetime
#from datetime import datetime
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
    CommentRepliesCountDto,
    CommentDto,
    PostsDetailsDto,
    DomainDetailsDto,
    DomainWithPostsDto
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
def domain_details_dto():
    domain_detailsdto=DomainDetailsDto(
        domain=DomainDto(
            domain_id=1,
            domain_name='django',
            description='django is one of the webframe work'
        ),
        domain_stats=DomainStatsDto(
            domain_id=1,
            followers_count=4,
            posts_count=5,
            bookmarked_count=2
        ),
        domain_experts=[
            UserDetailsDto(
                user_id=2,
                username='naveen',
                profile_pic='https://naveen.com/pic'
            )
        ],
        is_user_domain_expert=True,
        join_requests=[
            DomainJoinRequestDto(
                request_id=1,
                user_id=3
            )
        ],
        requested_users=[
            UserDetailsDto(
                user_id=3,
                username='daya',
                profile_pic='https://daya.com/pic'
            )
        ]
    )
    return domain_detailsdto


@pytest.fixture
def posts_dto():
    postdto = [
        PostDto(
            post_id=1,
            title='post1',
            content='post1 content',
            posted_at=datetime.datetime(2020, 6, 18, 0, 0),
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
    post_tag_details = PostTagDetailsDto(
            tags=tags_dto,
            post_tag_ids=post_tags_dto
        )
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

@pytest.fixture
def comment_reaction_count_dto():
    comment_reactionsdto = [
        CommentReactionsCountDto(
            comment_id=1,
            reactions_count=1
        )
    ]
    return comment_reactionsdto

@pytest.fixture
def comment_replies_count_dto():
    comment_repliesdto = [
        CommentRepliesCountDto(
            comment_id=1,
            replies_count=1
        )
    ]

@pytest.fixture
def users_dto():
    usersdto = [
        UserDetailsDto(
            user_id=1,
            username='chim',
            profile_pic='https://chim.com/pic'
        ),
        UserDetailsDto(
            user_id=2,
            username='kim',
            profile_pic='https://kim.com/pic'
        )
    ]
    return usersdto

@pytest.fixture
def comments_dto():
    commentsdto = [
        CommentDto(
            comment_id=1,
            content='content1',
            commented_at=datetime.datetime(2020, 6, 18, 0, 0),
            commented_by=2
        ),
        CommentDto(
            comment_id=2,
            content='content2',
            commented_at=datetime.datetime(2020, 6, 18, 0, 0),
            commented_by=1
        )
    ]
    return commentsdto

@pytest.fixture
def post_details_dto():
    postdetails = PostsDetailsDto(
        posts_dtos=[
            PostDto(
                post_id=1,
                title='post1',
                content='post1 content',
                posted_at=datetime.datetime(2020, 6, 18, 0, 0),
                posted_by=1
            )
        ],
        posts_reactions_count=[
            PostReactionsCountDto(
                post_id=1,
                reactions_count=2
            )
        ],
        posts_comments_count=[
            PostCommentsCountDto(
                post_id=1,
                comments_count=2
            )
        ],
        comments_reactions_count=[
            CommentReactionsCountDto(
                comment_id=1,
                reactions_count=1
            )
        ],
        comments_replies_count=None,
        comments_dto=[
            CommentDto(
                comment_id=1,
                content='content1',
                commented_at=datetime.datetime(2020, 6, 18, 0, 0),
                commented_by=2
            ),
            CommentDto(
                comment_id=2,
                content='content2',
                commented_at=datetime.datetime(2020, 6, 18, 0, 0),
                commented_by=1
            )
        ],
        post_tag_ids=[
            PostTagDto(
                post_id=1,
                tag_id=1
            )
        ],
        tags=[
            TagDto(
                tag_id=1,
                name='tag1'
            )
        ],
        users_dto=[
            UserDetailsDto(
                user_id=1,
                username='chim',
                profile_pic='https://chim.com/pic'
            ),
            UserDetailsDto(
                user_id=2,
                username='kim',
                profile_pic='https://kim.com/pic'
            )
        ]
    )
    return postdetails
