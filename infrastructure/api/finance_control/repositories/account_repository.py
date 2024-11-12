from uuid import UUID
from finance_control_service.application.user.user_dto import UserDTO
from finance_control_service.application.account.account_storage import AccountStorage
from finance_control_service.application.account.account_dto import AccountDTO
from finance_control.models import Account, User

class AccountRepository(AccountStorage):
    def _account_dto_to_model(self, account_dto: AccountDTO) -> Account:
        user = User.objects.get(pk=account_dto.user.id)
        
        account                 = Account()
        account.user            = user 
        account.name            = account_dto.name
        account.initial_balance = account_dto.initial_balance
        
        return account
    
    def _model_to_dto(self, account: Account) -> AccountDTO:
        user_dto = UserDTO(account.user.id, account.user.email, account.user.first_name, account.user.last_name)
        
        return AccountDTO({
            'id'             : account.id,
            'user'           : user_dto,
            'name'           : account.name,
            'initial_balance': account.initial_balance
        })
        
    def get_by_id(self, Account_id: UUID) -> AccountDTO:
        account = Account.objects.get(pk=Account_id)
        return self._model_to_dto(account)
    
    def get_all(self, user_id: UUID) -> list[AccountDTO]:
        accounts = Account.objects.filter(user_id=user_id)
        return [self._model_to_dto(account) for account in accounts]
    
    def save(self, account_dto: AccountDTO) -> AccountDTO:
        account = self._account_dto_to_model(account_dto)
        account.save()
        return self._model_to_dto(account)
    
    def update(self, account_dto: AccountDTO) -> AccountDTO:
        account = Account.objects.get(pk=account_dto.id)
        
        account.name = account_dto.name
        account.initial_balance = account_dto.initial_balance
        account.save()
        
        return self._model_to_dto(account)
    
    def delete(self, account_id: UUID) -> bool:
        account = Account.objects.get(pk=account_id)
        account.delete()
        return True