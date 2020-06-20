from formaster.exceptions.exceptions import (
    InvalidFormIdException,
    FormClosedException
)


class FromValidationMixer:

    def validate_form_id(self, form_id: int):
        valid_form_id = self.storage.validate_form_id(form_id)
        invalid_form_id = not valid_form_id
        if invalid_form_id:
            raise InvalidFormIdException(form_id)

    def validate_for_live_form(self, form_id: int):
        form_in_live = self.storage.validate_for_live_form(form_id)
        form_not_in_live = not form_in_live
        if form_not_in_live:
            raise FormClosedException
