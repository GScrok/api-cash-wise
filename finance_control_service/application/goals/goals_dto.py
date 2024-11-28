from finance_control_service.domain.goals.entities import Goal
from uuid import UUID
from datetime import datetime

from dataclasses import dataclass

@dataclass
class GoalDTO(object):
    
    id          : UUID
    name        : str
    user_id     : UUID
    category_id : UUID | None
    value       : float
    description : str
    start_at    : datetime
    end_at      : datetime
    
    def __init__(self, dict: dict) -> None:
        self.id          = dict.get('id')
        self.name        = dict.get('name')
        self.user_id     = dict.get('user_id')
        self.category_id = dict.get('category_id')
        self.value       = dict.get('value')
        self.description = dict.get('description')
        self.start_at    = dict.get('start_at')
        self.end_at      = dict.get('end_at')
    
    def to_domain(self) -> Goal:
        return Goal(self.__dict__)
    
    def to_dto(self, goal: Goal) -> 'GoalDTO':
        return GoalDTO(goal.__dict__)