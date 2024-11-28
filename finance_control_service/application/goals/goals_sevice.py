from finance_control_service.application.goals.goals_storage import GoalStorage
from finance_control_service.application.goals.goals_dto import GoalDTO
from finance_control_service.domain.goals.exceptions import *

from uuid import UUID

class GoalService(object):
    
    storage: GoalStorage
    
    def __init__(self, storage: GoalStorage) -> None:
        self.storage = storage
        
    def get_all(self) -> list[GoalDTO]:
        return self.storage.get_all()
    
    def get_all_by_category(self, category_id: UUID) -> list[GoalDTO]:
        return self.storage.get_all_by_category(category_id)
    
    def get_all_by_user(self, user_id: UUID) -> list[GoalDTO]:
        return self.storage.get_all_by_user(user_id)
    
    def get_by_id(self, id: UUID) -> GoalDTO:
        return self.storage.get_by_id(id)
    
    def create(self, goal_dto: GoalDTO) -> GoalDTO:
        if self.storage.verify_existing_by_name(goal_dto):
            raise GoalAlreadyExists('A goal with this name already exists.')
        
        goal = goal_dto.to_domain()
        goal.create()        
        final_dto = goal_dto.to_dto(goal)
        
        return self.storage.save(final_dto)
    
    def update(self, goal_dto: GoalDTO, id: UUID) -> GoalDTO:
        if self.storage.verify_existing_by_name_exclude_current(goal_dto, id):
            raise GoalAlreadyExists('A goal with this name already exists.')
        
        goal = goal_dto.to_domain()
        goal.update()
        final_dto = goal_dto.to_dto(goal)
        return self.storage.update(final_dto)
    
    def delete(self, id: UUID) -> bool:
        self.storage.delete(id)