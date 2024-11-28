from finance_control_service.domain.subcategories.entities import Subcategory
from uuid import UUID

from dataclasses import dataclass

@dataclass
class SubcategoryDTO(object):
    
    id          : UUID
    category_id : UUID
    name        : str
    description : str
    budget_limit: float
    
    def __init__(self, data: dict) -> None:
        
        self.id           = data.get('id')
        self.category_id  = data.get('category_id')
        self.name         = data.get('name')
        self.description  = data.get('description')
        self.budget_limit = data.get('budget_limit')
        
    def to_domain(self) -> Subcategory:
        return Subcategory(self.__dict__)
    
    def to_dto(self, subcategory: Subcategory) -> 'SubcategoryDTO':
        return  SubcategoryDTO({
            'id': subcategory.id,
            'category_id': subcategory.category_id,
            'name': subcategory.name,
            'description': subcategory.description,
            'budget_limit': subcategory.budget_limit
        })