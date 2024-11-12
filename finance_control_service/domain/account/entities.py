from uuid import UUID
from datetime import datetime
from finance_control_service.domain.user.entities import User
from finance_control_service.domain.account.exceptions import *

class Account(object):
    
    id: UUID
    user: User
    name: str
    initial_balance: float
    
    def __init__(self, data: dict) -> None:
        self.id              = data.get('id'),
        self.user            = data.get('user')
        self.initial_balance = data.get('initial_balance')
        
    def create(self):
        self.is_valid()
        
    def update(self):
        self.is_valid()
        
    def is_valid(self):
        if self.name is None:
            raise NameAccountIsRequired("The Name Account is Required!")
    