from finance_control_service.domain.user.entities import User
from .exceptions import *
from uuid import UUID

class Category(object):
    id: UUID
    name : str
    user : User
    description : str
    budget_limit : float
 
    def __init__(self, name, user: User, id=None, budget_limit=None, description=None):
        self.name = name
        self.user = user
        self.id = id
        self.description = description
        self.budget_limit = budget_limit

    def create(self):
        self.is_valid()

    def update(self):
        self.is_valid()

        if not self.id:
            raise CategoryUpdateRequiresExistingCategoryId('Cannot update a category without its Id')

    def is_valid(self):
        if self.budget_limit and self.budget_limit < 0:
            raise BudgetLimitCategoryMustBeGreaterThanZero('The category budget limit must be greater than zero')
        if self.name == '':
            raise NameCategoryCannotBeEmpty('The category name cannot be empty')
        if self.user is None:
            raise UserCategoryCannotBeEmpty('The category user cannot be empty')
        if self.description and len(self.description) > 250:
            raise DescriptionCategoryCannotBeGreaterThan250Characters('The category description cannot be greater than 250 characters')
