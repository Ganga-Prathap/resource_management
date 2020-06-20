import pytest
from unittest.mock import create_autospec
from formaster.interactors.mcq_question import MCQQuestionSubmitFormResponse
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)
from formaster.exceptions.exceptions import (
    InvalidQuestionIdException,
    QuestionDoesNotBelongToFormException,
    InvalidUserResponseSubmitException
)
from formaster.dtos.dtos import UserResponseDTO


def test_invalid_form_id_raise_exception():

    #Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    option_id = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.validate_form_id.return_value = False
    presenter.raise_exception_for_invalid_form_id.side_effect = NotFound

    interactor = MCQQuestionSubmitFormResponse(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id,
        user_submitted_option_id=option_id
    )

    #Act
    with pytest.raises(NotFound):
        interactor.base_form_submission_wrapper(
            presenter=presenter
        )

    #Assert
    storage.validate_form_id.assert_called_once_with(form_id)
    presenter.raise_exception_for_invalid_form_id.assert_called_once()
    call_obj = presenter.raise_exception_for_invalid_form_id.call_args
    error_obj = call_obj.args[0]
    assert error_obj.form_id == form_id


def test_form_closed_raise_exception():

    #Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    option_id = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.validate_for_live_form.return_value = False
    presenter.raise_exception_for_form_close.side_effect = BadRequest

    interactor = MCQQuestionSubmitFormResponse(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id,
        user_submitted_option_id=option_id
    )

    #Act
    with pytest.raises(BadRequest):
        interactor.base_form_submission_wrapper(
            presenter=presenter
        )

    #Assert
    storage.validate_form_id.assert_called_once_with(form_id)
    storage.validate_for_live_form.assert_called_once_with(form_id)
    presenter.raise_exception_for_form_close.assert_called_once()

def test_invalid_question_id_raise_exception():

    #Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    option_id = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.validate_question_id.side_effect = \
        InvalidQuestionIdException(question_id)
    presenter.raise_exception_for_invalid_question_id.side_effect = NotFound

    interactor = MCQQuestionSubmitFormResponse(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id,
        user_submitted_option_id=option_id
    )

    #Act
    with pytest.raises(NotFound):
        interactor.base_form_submission_wrapper(
            presenter=presenter
        )

    #Assert
    storage.validate_form_id.assert_called_once_with(form_id)
    storage.validate_for_live_form.assert_called_once_with(form_id)
    storage.validate_question_id.assert_called_once_with(question_id)
    presenter.raise_exception_for_invalid_question_id.assert_called_once()

def test_question_not_belongs_to_form_raise_exception():

    #Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    option_id = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.validate_form_question_id.side_effect = \
        QuestionDoesNotBelongToFormException(question_id)
    presenter.raise_exception_for_question_not_belongs_to_form.side_effect = \
        NotFound

    interactor = MCQQuestionSubmitFormResponse(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id,
        user_submitted_option_id=option_id
    )

    #Act
    with pytest.raises(NotFound):
        interactor.base_form_submission_wrapper(
            presenter=presenter
        )

    #Assert
    storage.validate_form_id.assert_called_once_with(form_id)
    storage.validate_for_live_form.assert_called_once_with(form_id)
    storage.validate_question_id.assert_called_once_with(question_id)
    storage.validate_form_question_id.assert_called_once_with(
        form_id, question_id
    )
    presenter.raise_exception_for_question_not_belongs_to_form.assert_called_once()

def test_invalid_user_submit_response_raise_exception():

    #Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    option_id = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_option_ids_for_question.return_value = [1, 3, 4]
    presenter.raise_exception_for_invalid_user_response_submit.side_effect = \
        NotFound

    interactor = MCQQuestionSubmitFormResponse(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id,
        user_submitted_option_id=option_id
    )

    #Act
    with pytest.raises(NotFound):
        interactor.base_form_submission_wrapper(
            presenter=presenter
        )

    #Assert
    storage.validate_form_id.assert_called_once_with(form_id)
    storage.validate_for_live_form.assert_called_once_with(form_id)
    storage.validate_question_id.assert_called_once_with(question_id)
    storage.validate_form_question_id.assert_called_once_with(
        form_id, question_id
    )
    storage.get_option_ids_for_question.assert_called_once_with(question_id)
    #presenter.raise_exception_for_invalid_user_response_submit.assert_called_once()
    call_obj = presenter.raise_exception_for_invalid_user_response_submit.call_args
    error_obj = call_obj.args[0]
    assert error_obj.user_answer == option_id


def test_mcq_question_submit_response():

    #Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    option_id = 2
    user_response_dto = UserResponseDTO(
        user_id=user_id,
        question_id = question_id,
        option_id=option_id
    )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_option_ids_for_question.return_value = [1, 2, 3]

    interactor = MCQQuestionSubmitFormResponse(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id,
        user_submitted_option_id=option_id
    )

    #Act
    interactor.base_form_submission_wrapper(
        presenter=presenter
    )

    #Assert
    storage.validate_form_id.assert_called_once_with(form_id)
    storage.validate_for_live_form.assert_called_once_with(form_id)
    storage.validate_question_id.assert_called_once_with(question_id)
    storage.validate_form_question_id.assert_called_once_with(
        form_id, question_id
    )
    storage.get_option_ids_for_question.assert_called_once_with(question_id)
    storage.create_user_mcq_response.assert_called_once_with(user_response_dto)
