from dataclasses import dataclass

@dataclass
class UserResponseDTO:
    user_id: int
    question_id: int
    option_id: int
