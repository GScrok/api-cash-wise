class SubcategoryAlreadyExists:
    def __init__(self, message: str):
        self.message = message
        
class SubcategoryUpdateRequiresExistingSubcategoryId:
    def __init__(self, message: str):
        self.message = message
        
class BudgetLimitSubcategoryMustBeGreaterThanZero:
    def __init__(self, messsage: str):
        self.message = messsage
        
class SubcategoryNeedsCategory:
    def __init__(self, message: str):
        self.message = message

class NameSubcategoryCannotBeEmpty:
    def __init__(self, message: str) -> None:
        self.message = message
        
class DescriptionSubcategoryCannotBeGreaterThan255Characters:
    def __init__(self, message: str) -> None:
        self.message = message