class InvalidFormIdException(Exception):
    def __init__(self, form_id):
        self.form_id = form_id

class FormClosedException(Exception):
    pass

class InvalidQuestionIdException(Exception):
    def __init__(self, question_id):
        self.question_id = question_id

class QuestionDoesNotBelongToFormException(Exception):
    def __init__(self, question_id):
        self.question_id = question_id

class InvalidUserResponseSubmitException(Exception):
    def __init__(self, user_answer):
        self.user_answer = user_answer
