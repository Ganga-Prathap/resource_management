from dataclasses import dataclass


@dataclass
class UserDto:
    user_id: int
    username: str
    is_admin: bool
