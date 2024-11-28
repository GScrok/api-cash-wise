from abc import ABC, abstractmethod
from finance_control_service.application.goals.goals_dto import GoalDTO
from uuid import UUID

class GoalStorage(ABC):
    
    @abstractmethod
    def save(self, goal_dto: GoalDTO) -> GoalDTO:
        print('aquiiiiiiii')
        
        pass
    
    @abstractmethod
    def get_all(self) -> list[GoalDTO]:
        pass
    
    @abstractmethod
    def get_all_by_category(self, category_id: int) -> list[GoalDTO]:
        pass
    
    @abstractmethod
    def get_all_by_user(self, user_id: int) -> list[GoalDTO]:
        pass

    @abstractmethod
    def get_by_id(self, goal_id: int) -> GoalDTO:
        pass

    @abstractmethod
    def verify_existing_by_name(self, goal_dto: GoalDTO) -> None:
        pass
    
    @abstractmethod
    def verify_existing_by_name_exclude_current(self, goal_dto: GoalDTO, pk: UUID) -> None:
        pass

    @abstractmethod
    def update(self, goal_dto: GoalDTO) -> GoalDTO:
        pass

    @abstractmethod
    def delete(self, goal_id: int) -> None:
        pass