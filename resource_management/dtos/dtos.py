from datetime import datetime
from dataclasses import dataclass
from resource_management.constants.enums import AccessLevelEnum

"""
@dataclass
class UserDto:
    user_id: int
    username: str
    email: str
    job_role: str
    department: str
    gender: str
    profile_pic: str
"""
@dataclass
class UserDto:
    user_id: int
    username: str
    is_admin: bool


@dataclass
class ResourceDto:
    resource_id: int
    resource_name: str
    description: str
    link: str
    thumbnail: str

@dataclass
class ItemDto:
    item_id: int
    title: str
    resource_name: str
    description: str
    link: str

@dataclass
class RequestDto:
    request_id: int
    user_id: int
    resource_name: str
    item_name: str
    access_level: AccessLevelEnum
    due_date_time: datetime
