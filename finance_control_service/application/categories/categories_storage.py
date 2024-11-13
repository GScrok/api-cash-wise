from abc import ABC, abstractmethod

from finance_control_service.application.categories.categories_dto import CategoryDTO

from uuid import UUID

class CategoryStorage(ABC):
    @abstractmethod
    def save(self, category_dto: CategoryDTO) -> CategoryDTO:
        pass

    @abstractmethod
    def get_all(self, user_id: int) -> list[CategoryDTO]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> CategoryDTO:
        pass

    @abstractmethod
    def verify_existing_category_by_name(self, category_dto: CategoryDTO) -> None:
        pass
    
    @abstractmethod
    def verify_existing_category_by_name_exclude_current(self, category_dto: CategoryDTO, pk: UUID) -> None:
        pass

    @abstractmethod
    def update(self, category_dto: CategoryDTO) -> CategoryDTO:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass