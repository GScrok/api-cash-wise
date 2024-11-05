from finance_control_service.domain.user.entities import User
from .exceptions import *

class Category(object):
    id: int
    name : str
    budget_limit : float
 
    def __init__(self, name, user: User, budget_limit=None):
        self.name = name
        self.user = user
        self.budget_limit = budget_limit
        self.id = None

    def create_category(self):
        self.is_valid()

    def update_category(self):
        pass

    def delete_category(self):
        pass

    def is_valid(self):
        if self.budget_limit and self.budget_limit < 0:
            raise BudgetLimitMustBeGreaterThanZero('The budget limit must be greater than zero')