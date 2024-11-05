from finance_control_service.domain.categories.entities import Category
from finance_control_service.domain.user.entities import User

class CategoryDto(object):
    id: int
    name : str
    user : User
    budget_limit : float

    def __init__(self, name, user: User, budget_limit=None):
        self.name = name
        self.user = user
        self.budget_limit = budget_limit
        self.id = None

    def to_domain(self):
        category = Category(self.name, self.user, self.budget_limit)
        category.id = self.id
        return category
    
    def to_dto(self, category: Category):
        category_dto = CategoryDto(category.id, category.user, category.budget_limit)
        return category_dto