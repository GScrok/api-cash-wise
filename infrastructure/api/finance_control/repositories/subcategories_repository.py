from finance_control_service.application.user.user_dto import UserDTO
from finance_control_service.application.categories.categories_dto import CategoryDTO
from finance_control_service.application.subcategories.subcategories_storage import SubcategoryStorage
from finance_control_service.application.subcategories.subcategories_dto import SubcategoryDTO
from finance_control.models import Subcategory, Category

from uuid import UUID

class SubcategoryRepository(SubcategoryStorage):
    
    def _dto_to_model(self, subcategory_dto: SubcategoryDTO) -> Subcategory:
        category = Category.objects.get(pk=subcategory_dto.category.id)
        
        subcategory              = Subcategory()
        subcategory.id           = subcategory_dto.id
        subcategory.category     = category
        subcategory.name         = subcategory_dto.name
        subcategory.description  = subcategory_dto.description
        subcategory.budget_limit = subcategory_dto.budget_limit
        
        return subcategory
    
    def _model_to_dto(self, subcategory: Subcategory) -> SubcategoryDTO:
        user_dto = UserDTO(subcategory.category.user.id, subcategory.category.user.email, subcategory.category.user.first_name, subcategory.category.user.last_name)
        
        category_dto = CategoryDTO({
            'id'          : subcategory.category.id,
            'name'        : subcategory.category.name,
            'user'        : user_dto,
            'budget_limit': subcategory.category.budget_limit,
            'description' : subcategory.category.description
        })
        
        return SubcategoryDTO({
            'id'          : subcategory.id,
            'category'    : category_dto,
            'name'        : subcategory.name,
            'budget_limit': subcategory.budget_limit,
            'description' : subcategory.description,
        })
        
    def verify_existing_by_name(self, subcategory_dto: SubcategoryDTO) -> bool:
        exists = Subcategory.objects.filter(
            name=subcategory_dto.name,
            category_id=subcategory_dto.category.id
        ).first()
        
        return exists is not None
    
    def verify_existing_by_name_exclude_current(self, subcategory_dto: SubcategoryDTO, pk: UUID) -> bool:
        exists = Subcategory.objects.filter(
            name=subcategory_dto.name,
            categoty_id=subcategory_dto.category.id 
        ).exclude(pk=pk).first()
        
        return exists is not None
    
    def get_by_id(self, id: UUID) -> SubcategoryDTO:
        return self._model_to_dto(Subcategory.objects.get(pk=id))
    
    def get_all(self) -> list[SubcategoryDTO]:
        subcategories = Subcategory.objects.all()
        return [self._model_to_dto(subcategory) for subcategory in subcategories]

    def get_all_by_category(self, category_id: UUID) -> list[SubcategoryDTO]:
        subcategories = Subcategory.objects.filter(category_id=category_id)
        return [self._model_to_dto(subcategory) for subcategory in subcategories]
    
    def save(self, subcategory_dto: SubcategoryDTO) -> SubcategoryDTO:
        subcategory = self._dto_to_model(subcategory_dto)
        subcategory.save()
        return self._model_to_dto(subcategory)
    
    def update(self, subcategory_dto: SubcategoryDTO) -> SubcategoryDTO:
        subcategory = self._dto_to_model(subcategory_dto)
        
        subcategory.name = subcategory_dto.name
        subcategory.budget_limit = subcategory_dto.budget_limit
        subcategory.description = subcategory_dto.description
        subcategory.save()
        
        return self._model_to_dto(subcategory)
    
    def delete(self, id: UUID) -> bool:
        subcategory = Subcategory.objects.get(pk=id)
        subcategory.delete()
        return True