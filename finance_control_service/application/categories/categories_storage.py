from abc import ABC, abstractmethod

from finance_control_service.application.categories.categories_dto import CategoryDto

class CategoryStorage(ABC):
    @abstractmethod
    def save_category(self) -> CategoryDto:
        pass

    @abstractmethod
    def get_all_categories(self, user_id: int) -> list[CategoryDto]:
        pass

    @abstractmethod
    def get_category_by_id(self, category_id: int) -> CategoryDto:
        pass

    @abstractmethod
    def update_category(self, category_dto: CategoryDto) -> CategoryDto:
        pass

    @abstractmethod
    def delete_category(self, category_id: int) -> None:
        pass