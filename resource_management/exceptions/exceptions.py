class UserDoesNotExist(Exception):
    pass

class InvalidPassword(Exception):
    pass

class UnAuthorizedUserException(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


class UserNameAlreadyExist(Exception):
    pass

class UserNotAllowedToCreate(Exception):
    pass

class InvalidResourceIdException(Exception):
    def __init__(self, resource_id):
        self.resource_id = resource_id

class InvalidItemIdException(Exception):
    def __init__(self, item_id):
        self.item_id = item_id

class UserNotAllowedToUpdate(Exception):
    pass

class InvalidOffsetException(Exception):
    def __init__(self, offset):
        self.offset = offset

class InvalidLimitException(Exception):
    def __init__(self, limit):
        self.limit = limit

class InvalidUserException(Exception):
    def __init__(self, user_id):
        self.user_id = user_id

class InvalidItemIds(Exception):
    def __init__(self, item_ids):
        self.item_ids = item_ids
