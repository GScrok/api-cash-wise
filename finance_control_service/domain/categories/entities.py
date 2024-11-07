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

    def create_category(self):
        self.is_valid()

    def update_category(self):
        self.is_valid()

        if not self.id:
            raise CategoryUpdateRequiresExistingCategoryId('Cannot update a record without its Id')

    def is_valid(self):
        print(self.id)
        if self.budget_limit and self.budget_limit < 0:
            raise BudgetLimitMustBeGreaterThanZero('The budget limit must be greater than zero')
        if self.name == '':
            raise NameCannotBeEmpty('The name cannot be empty')
        if self.user is None:
            raise UserCannotBeEmpty('The user cannot be empty')
        if self.description and len(self.description) > 250:
            raise DescriptionCannotBeGreaterThan250Characters('The description cannot be greater than 250 characters')
