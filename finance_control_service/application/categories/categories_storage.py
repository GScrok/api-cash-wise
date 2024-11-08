from abc import ABC, abstractmethod

from finance_control_service.application.categories.categories_dto import CategoryDto

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
    def update(self, category_dto: CategoryDto) -> CategoryDto:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass