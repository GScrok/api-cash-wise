class SubcategoryAlreadyExists(Exception):
    def __init__(self, message: str):
        self.message = message
        
class SubcategoryUpdateRequiresExistingSubcategoryId(Exception):
    def __init__(self, message: str):
        self.message = message
        
class BudgetLimitSubcategoryMustBeGreaterThanZero(Exception):
    def __init__(self, messsage: str):
        self.message = messsage
        
class SubcategoryNeedsCategory(Exception):
    def __init__(self, message: str):
        self.message = message

class NameSubcategoryCannotBeEmpty(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        
class DescriptionSubcategoryCannotBeGreaterThan255Characters(Exception):
    def __init__(self, message: str) -> None:
        self.message = message