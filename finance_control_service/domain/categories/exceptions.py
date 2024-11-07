class BudgetLimitMustBeGreaterThanZero(Exception):
    def __init__(self, message):
        self.message = message

class NameCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class UserCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class DescriptionCannotBeGreaterThan250Characters(Exception):
    def __init__(self, message):
        self.message = message

class CategoryUpdateRequiresExistingCategoryId(Exception):
    def __init__(self, message):
        self.message = message

