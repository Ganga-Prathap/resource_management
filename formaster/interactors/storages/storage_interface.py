from abc import abstractmethod
from typing import List
from formaster.dtos.dtos import UserResponseDTO


class StorageInterface:

    @abstractmethod
    def validate_form_id(self, form_id: int) -> bool:
        pass

    @abstractmethod
    def validate_for_live_form(self, form_id: int) -> bool:
        pass

    @abstractmethod
    def validate_question_id(self, question_id: int):
        pass

    @abstractmethod
    def validate_form_question_id(self, form_id: int, question_id: int):
        pass

    @abstractmethod
    def get_option_ids_for_question(self, question_id: int) -> List[int]:
        pass

    @abstractmethod
    def create_user_mcq_response(self, user_response_dto: UserResponseDTO):
        pass
