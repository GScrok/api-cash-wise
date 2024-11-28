from finance_control_service.application.subcategories.subcategories_storage import SubcategoryStorage
from finance_control_service.application.subcategories.subcategories_dto import SubcategoryDTO
from finance_control_service.domain.subcategories.exceptions import *

from uuid import UUID

class SubcategoryService(object):
    
    storage: SubcategoryStorage
    
    def __init__(self, storage: SubcategoryStorage) -> None:
        self.storage = storage
        
    def get_all(self) -> list[SubcategoryDTO]:
        return self.storage.get_all()
    
    def get_all_by_category(self, category_id: UUID) -> list[SubcategoryDTO]:
        return self.storage.get_all(category_id)
    
    def get_by_id(self, id: UUID) -> SubcategoryDTO:
        return self.storage.get_by_id(id)
    
    def create(self, subcategory_dto: SubcategoryDTO) -> SubcategoryDTO:
        if self.storage.verify_existing_by_name(subcategory_dto):
            raise SubcategoryAlreadyExists('A subcategory with this name already exists.')
        
        subcategory = subcategory_dto.to_domain()
        subcategory.create()
        final_dto = subcategory_dto.to_dto(subcategory)
        return self.storage.save(final_dto)
    
    def update(self, subcategory_dto: SubcategoryDTO, id: UUID) -> SubcategoryDTO:
        if self.storage.verify_existing_by_name_exclude_current(subcategory_dto, id):
            raise SubcategoryAlreadyExists('A subcategory with this name already exists.')
        
        subcategory = subcategory_dto.to_domain()
        subcategory.update()
        final_dto = subcategory_dto.to_dto(subcategory)
        return self.storage.update(final_dto)
    
    def delete(self, id: UUID) -> bool:
        self.storage.delete(id)