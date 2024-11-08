from finance_control_service.application.categories.categories_dto import CategoryDto
from finance_control_service.application.categories.categories_storage import CategoryStorage
from finance_control_service.application.user.user_dto import UserDTO
from ..models import Category, User

from uuid import UUID 

class CategoryRepository(CategoryStorage):
    def _category_dto_to_model(self, category_dto: CategoryDto):
        user = User.objects.get(pk=category_dto.user.id)

        category = Category()
        category.name = category_dto.name
        category.user = user
        category.budget_limit = category_dto.budget_limit
        category.description = category_dto.description
        return category

    def _model_to_dto(self, category: Category):
        user_dto = UserDTO(category.user.id, category.user.email, category.user.first_name, category.user.last_name)

        category_dto = CategoryDto(
            {
                'name': category.name,
                'id': category.id,
                'user': user_dto,
                'budget_limit': category.budget_limit,
                'description': category.description,
            },
        )
        return category_dto

    def get_by_id(self, category_id: UUID):
        category = Category.objects.get(pk=category_id)
        return self._model_to_dto(category)
    
    def get_all(self, user_id: int):
        categories = Category.objects.filter(user_id=user_id)
        return [self._model_to_dto(category) for category in categories]

    def save(self, category_dto: CategoryDto):
        category = self._category_dto_to_model(category_dto)
        category.save()
        return self._model_to_dto(category)
    
    def update(self, category_dto: CategoryDto):
        category = self._category_dto_to_model(category_dto)
        category.save()
        return self._model_to_dto(category)
    
    def delete(self, category_id: int):
        category = Category.objects.get(pk=category_id)
        category.delete()
