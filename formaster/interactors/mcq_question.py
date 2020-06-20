from formaster.interactors.base import BaseFormSubmissionInteractor
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.exceptions.exceptions import InvalidUserResponseSubmitException
from formaster.dtos.dtos import UserResponseDTO


class MCQQuestionSubmitFormResponse(BaseFormSubmissionInteractor):

    def __init__(self, storage: StorageInterface,
                 form_id: int, question_id: int, user_id: int,
                 user_submitted_option_id: int):
        super().__init__(storage, form_id, question_id, user_id)
        self.user_submitted_option_id = user_submitted_option_id

    def _validate_user_respose(self):
        option_ids = self.storage.get_option_ids_for_question(self.question_id)
        if self.user_submitted_option_id not in option_ids:
            raise InvalidUserResponseSubmitException(
                self.user_submitted_option_id
            )

    def _create_user_response(self):
        user_response_dto = UserResponseDTO(
                                user_id=self.user_id,
                                question_id=self.question_id,
                                option_id=self.user_submitted_option_id
                            )
        self.storage.create_user_mcq_response(user_response_dto)
