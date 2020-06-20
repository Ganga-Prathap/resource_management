class InvalidMealIdException(Exception):
    def __init__(self, meal_id):
        self.meal_id = meal_id

class TimeOutException(Exception):
    pass

class ItemIdsDuplicationException(Exception):
    
    def __init__(self, duplicate_item_ids):
        self.duplicate_item_ids = duplicate_item_ids
    pass

class InvalidItemIdsException(Exception):
    def __init__(self, invalid_item_ids):
        self.invalid_item_ids = invalid_item_ids

class InvalidItemQuantityException(Exception):
    pass
