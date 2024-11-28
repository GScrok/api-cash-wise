from .exceptions import *
from uuid import UUID
from finance_control_service.domain.user.entities import User
from datetime import datetime

class Goal(object):
    
    id          : UUID
    name        : str
    user_id     : User
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
        
    def create(self):        
        self.is_valid()
        
    def update(self):
        self.is_valid()
        
        if not self.id:
            raise GoalUpdateRequiresExistingGoalId('Cannot update a goal without its Id')
        
    def is_valid(self):
        if self.name is None:
            raise GoalNameCannotBeNull('The goal name cannot be null')
        if self.user_id is None:
            raise UserGoalCannotBeEmpty('The goal user cannot be empty')
        if self.value <= 0:
            raise GoalValueMustBeGreaterThanZero('The goal amount must be greater than zero')
        if not self.description:
            raise DescriptionGoalCannotBeEmpty('The goal description cannot be empty')
        if len(self.description) > 250:
            raise DescriptionGoalCannotBeGreaterThan250Characters('The goal description cannot be greater than 250 characters')
        if self.start_at > self.end_at:
            raise GoalStartAtCannotBeGreaterThanEndAt('The Goal start_at cannot be greater than end_at')