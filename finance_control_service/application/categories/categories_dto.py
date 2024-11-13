from finance_control_service.domain.categories.entities import Category
from finance_control_service.application.user.user_dto import UserDTO
from uuid import UUID

from dataclasses import dataclass

@dataclass
class CategoryDTO(object):
    id: UUID
    name : str
    user : UserDTO
    description : str
    budget_limit : float

    def __init__(self, dict: dict):
        self.name = dict.get('name')
        self.user = dict.get('user')
        self.id = dict.get('id')
        self.budget_limit = dict.get('budget_limit')
        self.description = dict.get('description')

    def to_domain(self):
        category = Category(self.name, self.user, self.id, self.budget_limit, self.description)
        return category
    
    def to_dto(self, category: Category):
        user_dto = UserDTO(category.user.id, category.user.email, category.user.first_name, category.user.last_name)

        dict = {
            'name': category.name,
            'user': user_dto,
            'id': category.id,
            'budget_limit': category.budget_limit,
            'description': category.description
        }
        category_dto = CategoryDTO(dict)
        return category_dto