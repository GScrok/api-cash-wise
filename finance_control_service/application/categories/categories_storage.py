from abc import ABC, abstractmethod
from .categories_dto import CategoryDto

class CategoryStorage(ABC):
    @abstractmethod
    def save_category(self):
        pass

    @abstractmethod
    def get_all_categories(self):
        pass