from finance_control_service.domain.categories.entities import Category
from finance_control_service.domain.subcategories.exceptions import *
from uuid import UUID

class Subcategory(object):
    
    id          : UUID
    category_id : UUID
    name        : str
    description : str
    budget_limit: float
    
    def __init__(self, data: dict) -> None:
        
        self.id           = data.get('id')
        self.category_id     = data.get('category_id')
        self.name         = data.get('name')
        self.description  = data.get('description')
        self.budget_limit = data.get('budget_limit')
        
    def create(self):
        self.is_valid()
        
    def update(self):
        self.is_valid()
        
        if not self.id:
            raise SubcategoryUpdateRequiresExistingSubcategoryId('Cannot update a category without its Id')
        
    def is_valid(self):
        if self.budget_limit and self.budget_limit < 0:
            raise BudgetLimitSubcategoryMustBeGreaterThanZero('The subcategory budget limit must be greater than zero')
        
        if not self.category_id:
            raise SubcategoryNeedsCategory('Cannot create a subcategory without a category id')
        
        if not self.name:
            raise NameSubcategoryCannotBeEmpty('The subcategory name cannot be empty')
        
        if self.description and len(self.description) > 255:
            raise DescriptionSubcategoryCannotBeGreaterThan255Characters('The subcategory description cannot be greater than 255 characters')