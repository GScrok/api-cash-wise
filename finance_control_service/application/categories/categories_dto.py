from finance_control_service.domain.categories.entities import Category
from finance_control_service.application.user.user_dto import UserDTO
from uuid import UUID

from dataclasses import dataclass

@dataclass
class CategoryDto(object):
    id: UUID
    name : str
    user : UserDTO
    description : str
    budget_limit : float

    def __init__(self, name, user: UserDTO, id=None, budget_limit=None, description=None):
        self.name = name
        self.user = user
        self.id = id
        self.budget_limit = budget_limit
        self.description = description

    def to_domain(self):
        category = Category(self.name, self.user, self.id, self.budget_limit, self.description)
        return category
    
    def to_dto(self, category: Category):
        category_dto = CategoryDto(category.name, category.user, category.id, category.budget_limit, category.description)
        return category_dto