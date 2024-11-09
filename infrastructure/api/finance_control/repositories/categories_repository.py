from finance_control_service.application.categories.categories_dto import CategoryDto
from finance_control_service.application.categories.categories_storage import CategoryStorage
from finance_control_service.application.user.user_dto import UserDTO
from finance_control.models import Category, User

from uuid import UUID 

class CategoryRepository(CategoryStorage):
    def _category_dto_to_model(self, category_dto: CategoryDto):
        user = User.objects.get(pk=category_dto.user.id)

        category = Category()
        category.id = category_dto.id
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

    def verify_existing_category_by_name(self, category_dto: CategoryDto) -> bool:
        existing_category = Category.objects.filter(
            name=category_dto.name,
            user_id=category_dto.user.id
        ).first()
        
        return existing_category is not None

    def verify_existing_category_by_name_exclude_current(self, category_dto: CategoryDto, pk: UUID) -> bool:
        existing_category = Category.objects.filter(
            name=category_dto.name,
            user_id=category_dto.user.id
        ).exclude(pk=pk).first()
        
        return existing_category is not None

    def get_by_id(self, category_id: UUID):
        category = Category.objects.get(pk=category_id)
        return self._model_to_dto(category)
    
    def get_all(self, user_id: UUID):
        categories = Category.objects.filter(user_id=user_id)
        return [self._model_to_dto(category) for category in categories]

    def save(self, category_dto: CategoryDto):
        category = self._category_dto_to_model(category_dto)
        category.save()
        return self._model_to_dto(category)
    
    def update(self, category_dto: CategoryDto):
        category = Category.objects.get(pk=category_dto.id)
        
        category.name = category_dto.name
        category.budget_limit = category_dto.budget_limit
        category.description = category_dto.description
        category.save()
        
        return self._model_to_dto(category)
        
    def delete(self, category_id: UUID):
        category = Category.objects.get(pk=category_id)
        category.delete()
