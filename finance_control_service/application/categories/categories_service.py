from finance_control_service.application.categories.categories_dto import CategoryDto
from .categories_storage import CategoryStorage
from finance_control_service.domain.categories.exceptions import *

class CategoryService(object):
    storage: CategoryStorage

    def __init__(self, storage: CategoryStorage):
        self.storage = storage

    def get_all(self, user_id: int):
        return self.storage.get_all(user_id)
    
    def get_by_id(self, category_id: int):
        return self.storage.get_by_id(category_id)
    
    def create(self, category_dto: CategoryDto):
        category = category_dto.to_domain()
        category.create()
        final_dto = category_dto.to_dto(category)
        return self.storage.save(final_dto)

    def update(self, category_dto: CategoryDto):
        category = category_dto.to_domain()
        category.update()
        final_dto = category_dto.to_dto(category)
        return self.storage.update(final_dto)
        
    def delete(self, category_id: int):
        self.storage.delete(category_id)
