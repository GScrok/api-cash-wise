class GoalException(Exception):
    def __init__(self, message):
        self.message = message
        
class GoalUpdateRequiresExistingGoalId(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

class UserGoalCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class CategoryGoalCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class TypeGoalCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class AmountGoalCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class DescriptionGoalCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class GoalDateMustBeValid(Exception):
    def __init__(self, message):
        self.message = message

class DescriptionGoalCannotBeGreaterThan250Characters(Exception):
    def __init__(self, message):
        self.message = message

class GoalValueMustBeGreaterThanZero(Exception):
    def __init__(self, message):
        self.message = message
        
class GoalNameCannotBeNull(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

class GoalStartAtCannotBeGreaterThanEndAt():
    def __init__(self, message) -> None:
        self.message = message
        
class GoalAlreadyExists(Exception):
    def __init__(self, message: str):
        self.message = message