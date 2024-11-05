from finance_control_service.application.user.user_dto import UserDto
from finance_control_service.application.categories.categories_dto import CategoryDto
from .categories_storage import CategoryStorage
from finance_control_service.domain.categories.exceptions import *

class CategoryService(object):
    storage: CategoryStorage

    def __init__(self, storage: CategoryStorage):
        self.storage = storage

    def get_categories(self, user_dto: UserDto):
        return self.storage.get_all_categories(user_dto.id)
    
    def create_new_category(self, category_dto: CategoryDto):
        category = category_dto.to_domain()
        try:
            category.create_category()
            final_dto = category_dto.to_dto(category)
            self.storage.save_category(final_dto)

        except BudgetLimitMustBeGreaterThanZero as e:
            return {'message': e, 'code': str(type(e))}