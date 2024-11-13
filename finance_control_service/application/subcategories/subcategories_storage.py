from abc import ABC, abstractmethod

from finance_control_service.application.subcategories.subcategories_dto import SubcategoryDTO

from uuid import UUID

class SubcategoryStorage(ABC):
    
    @abstractmethod
    def save(self, subcategory_dto: SubcategoryDTO) -> SubcategoryDTO:
        pass
    
    @abstractmethod
    def get_all(self, category_id: int) -> list[SubcategoryDTO]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> SubcategoryDTO:
        pass

    @abstractmethod
    def verify_existing_by_name(self, category_dto: SubcategoryDTO) -> None:
        pass
    
    @abstractmethod
    def verify_existing_by_name_exclude_current(self, category_dto: SubcategoryDTO, pk: UUID) -> None:
        pass

    @abstractmethod
    def update(self, category_dto: SubcategoryDTO) -> SubcategoryDTO:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass