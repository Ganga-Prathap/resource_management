from abc import abstractmethod
from formaster.exceptions.exceptions import (
    InvalidFormIdException,
    InvalidQuestionIdException,
    QuestionDoesNotBelongToFormException,
    InvalidUserResponseSubmitException
)


class PresenterInterface:

    @abstractmethod
    def raise_exception_for_invalid_form_id(
            self,
            error: InvalidFormIdException):
        pass

    @abstractmethod
    def raise_exception_for_form_close(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_question_id(
            self,
            error: InvalidQuestionIdException):
        pass

    @abstractmethod
    def raise_exception_for_question_not_belongs_to_form(
            self,
            error: QuestionDoesNotBelongToFormException):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_response_submit(
            self,
            error: InvalidUserResponseSubmitException):
        pass
