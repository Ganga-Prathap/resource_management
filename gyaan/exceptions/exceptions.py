class InvalidDomainIdException(Exception):
    def __init__(self, domain_id: int):
        self.domain_id = domain_id

class DomainUnfollowedUserException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id

class InvalidPostidsException(Exception):
    def __init__(self, post_ids):
        self.post_ids = post_ids
