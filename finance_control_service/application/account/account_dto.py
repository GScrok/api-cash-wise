from dataclasses import dataclass
from uuid import UUID
from finance_control_service.application.user.user_dto import UserDTO
from finance_control_service.domain.account.entities import Account

@dataclass
class AccountDTO(object):
    
    id: UUID
    user: UserDTO
    name: str
    initial_balance: float
    
    def __init__(self, data: dict) -> None :
        self.id              = data.get('id')
        self.user            = data.get('user')
        self.name            = data.get('name')
        self.initial_balance = data.get('initial_balance')
        
    def to_domain(self) -> Account:
        return Account(self.__dict__)
    
    def to_dto(self, account: Account):
        user_dto = UserDTO(account.user.id, account.user.email, account.user.first_name, account.user.last_name)
        dict = {
            'id'             : account.id,
            'user'           : user_dto,
            'name'           : account.name,
            'initial_balance': account.initial_balance
        }
        return AccountDTO(dict)