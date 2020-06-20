from formaster.interactors.storages.storage_interface import StorageInterface
from abc import abstractmethod
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import (
    InvalidFormIdException,
    FormClosedException,
    InvalidQuestionIdException,
    QuestionDoesNotBelongToFormException,
    InvalidUserResponseSubmitException
)
from formaster.interactors.form_validation_mixer import FromValidationMixer

class BaseFormSubmissionInteractor(FromValidationMixer):

    def __init__(self, storage: StorageInterface,
                 form_id: int, question_id: int,
                 user_id: int):
        self.storage = storage
        self.form_id = form_id
        self.question_id = question_id
        self.user_id = user_id

    def base_form_submission_wrapper(self, presenter: PresenterInterface):
        try:
            self.base_form_submission_response()
        except InvalidFormIdException as error:
            presenter.raise_exception_for_invalid_form_id(error)
        except FormClosedException:
            presenter.raise_exception_for_form_close()
        except InvalidQuestionIdException as error:
            presenter.raise_exception_for_invalid_question_id(error)
        except QuestionDoesNotBelongToFormException as error:
            presenter.raise_exception_for_question_not_belongs_to_form(error)
        except InvalidUserResponseSubmitException as error:
            presenter.raise_exception_for_invalid_user_response_submit(error)

    def base_form_submission_response(self):
        self.validate_form_id(self.form_id)
        self.validate_for_live_form(self.form_id)
        self.storage.validate_question_id(self.question_id)
        self.storage.validate_form_question_id(self.form_id, self.question_id)
        self._validate_user_respose()
        self._create_user_response()

    @abstractmethod
    def _validate_user_respose(self):
        pass

    @abstractmethod
    def _create_user_response(self):
        pass
