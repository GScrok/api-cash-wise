from finance_control_service.application.categories.categories_dto import CategoryDto
from .categories_storage import CategoryStorage
from finance_control_service.domain.categories.exceptions import *

class CategoryService(object):
    storage: CategoryStorage

    def __init__(self, storage: CategoryStorage):
        self.storage = storage

    def get_all_categories(self, user_id: int):
        return self.storage.get_all_categories(user_id)
    
    def get_category_by_id(self, category_id: int):
        return self.storage.get_category_by_id(category_id)
    
    def create_new_category(self, category_dto: CategoryDto):
        category = category_dto.to_domain()
        category.create_category()
        final_dto = category_dto.to_dto(category)
        return self.storage.save_category(final_dto)

    def update_category(self, category_dto: CategoryDto):
        category = category_dto.to_domain()
        category.update_category()
        final_dto = category_dto.to_dto(category)
        print(f'final_dto { final_dto}')
        return self.storage.update_category(final_dto)
        
    def delete_category(self, category_id: int):
        self.storage.delete_category(category_id)
