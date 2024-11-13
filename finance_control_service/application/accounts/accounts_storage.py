from abc import ABC, abstractmethod
from uuid import UUID

from finance_control_service.application.accounts.accounts_dto import AccountDTO

class AccountStorage(ABC):
    
    @abstractmethod
    def save(self, account_dto: AccountDTO) -> AccountDTO:
        pass
    
    @abstractmethod
    def update(self, account_dto: AccountDTO) -> AccountDTO:
        pass

    @abstractmethod
    def delete(self, account_id: UUID) -> bool:
        pass
    
    @abstractmethod
    def get_all(self, user_id: UUID) -> list[AccountDTO]:
        pass
    
    @abstractmethod
    def get_by_id(self, Account_id: UUID) -> AccountDTO:
        pass