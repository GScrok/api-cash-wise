from finance_control_service.domain.subcategory.entities import Subcategory
from finance_control_service.application.subcategory.subcategory_dto import SubcategoryDTO
from finance_control_service.application.categories.categories_dto import CategoryDto
from finance_control_service.application.user.user_dto import UserDTO
from uuid import UUID

from dataclasses import dataclass

@dataclass
class SubcategoryDTO(object):
    
    id          : UUID
    category    : CategoryDto
    name        : str
    description : str
    budget_limit: float
    
    def __init__(self, data: dict) -> None:
        
        self.id           = data.get('id')
        self.category     = data.get('category')
        self.name         = data.get('name')
        self.description  = data.get('description')
        self.budget_limit = data.get('budget_limit')
        
    def to_domain(self) -> Subcategory:
        return Subcategory(self.__dict__)
    
    def to_dto(self, subcategory: Subcategory) -> SubcategoryDTO:

        user_dto = UserDTO(
            id=subcategory.category.user.id,
            email=subcategory.category.user.email,
            first_name=subcategory.category.user.first_name,
            last_name=subcategory.category.user.last_name
        )
        
        category_dto = CategoryDto({
            'id': subcategory.category.id,
            'name': subcategory.category.name,
            'user': user_dto,
            'budget_limit': subcategory.category.budget_limit,
            'description': subcategory.category.description
        })
        
        return  SubcategoryDTO({
            'id': subcategory.id,
            'category': category_dto,
            'name': subcategory.name,
            'description': subcategory.description,
            'budget_limit': subcategory.budget_limit
        })