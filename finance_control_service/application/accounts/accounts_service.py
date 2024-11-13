from finance_control_service.application.accounts.accounts_storage import AccountStorage
from finance_control_service.application.accounts.accounts_dto import AccountDTO
from uuid import UUID

class AccountService(object):
    storage: AccountStorage
    
    def __init__(self, storage: AccountStorage) -> None:
        self.storage = storage
        
    def get_all(self, user_id: UUID) -> list[AccountDTO]:
        return self.storage.get_all(user_id)
    
    def get_by_id(self, account_id: UUID) -> AccountDTO:
        return self.storage.get_by_id(account_id)
    
    def create(self, account_dto: AccountDTO) -> AccountDTO:
        account = account_dto.to_domain()
        account.create()
        return self.storage.save(account_dto.to_dto(account))
    
    def update(self, account_dto: AccountDTO, id: UUID) -> AccountDTO:
        account = account_dto.to_domain()
        account.update()
        return self.storage.update(account_dto.to_dto(account))
    
    def delete(self, account_id: UUID) -> bool:
        self.storage.delete(account_id)
        return True