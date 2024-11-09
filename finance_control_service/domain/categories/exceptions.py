class BudgetLimitCategoryMustBeGreaterThanZero(Exception):
    def __init__(self, message):
        self.message = message

class NameCategoryCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class UserCategoryCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class DescriptionCategoryCannotBeGreaterThan250Characters(Exception):
    def __init__(self, message):
        self.message = message

class CategoryUpdateRequiresExistingCategoryId(Exception):
    def __init__(self, message):
        self.message = message

class CategoryAlreadyExists(Exception):
    def __init__(self, message):
        self.message = message

