class UserDoesNotExist(Exception):
    pass

class InvalidPassword(Exception):
    pass

class UnAuthorizedUserException(Exception):
    pass

class UserNameAlreadyExist(Exception):
    pass

class UserNotAllowedToCreate(Exception):
    pass

class InvalidResourceException(Exception):
    pass

class InvalidItem(Exception):
    pass

class UserNotAllowedToUpdate(Exception):
    pass
