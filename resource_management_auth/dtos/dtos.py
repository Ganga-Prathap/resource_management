from dataclasses import dataclass


@dataclass
class UserDto:
    user_id: int
    username: str
    is_admin: bool

@dataclass
class UserInfoDto:
    user_id: int
    username: str
    email: str
    job_role: str
    department: str
    gender: str
    profile_pic: str
