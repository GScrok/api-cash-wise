from abc import ABC, abstractmethod

from finance_control_service.application.categories.categories_dto import CategoryDto

from uuid import UUID

class CategoryStorage(ABC):
    @abstractmethod
    def save(self, category_dto: CategoryDto) -> CategoryDto:
        pass

    @abstractmethod
    def get_all(self, user_id: int) -> list[CategoryDto]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> CategoryDto:
        pass

    @abstractmethod
    def verify_existing_category_by_name(self, category_dto: CategoryDto) -> None:
        pass
    
    @abstractmethod
    def verify_existing_category_by_name_exclude_current(self, category_dto: CategoryDto, pk: UUID) -> None:
        pass

    @abstractmethod
    def update(self, category_dto: CategoryDto) -> CategoryDto:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass