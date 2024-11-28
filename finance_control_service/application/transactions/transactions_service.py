from finance_control_service.application.transactions.transactions_dto import TransactionDTO
from finance_control_service.domain.transactions.exceptions import *
from .transactions_storage import TransactionStorage

from uuid import UUID

class TransactionService(object):
    storage: TransactionStorage

    def __init__(self, storage: TransactionStorage):
        self.storage = storage

    def get_all(self, user_id: UUID):
        return self.storage.get_all(user_id)
    
    def get_all_by_category(self, category_id: UUID, user_id: UUID):
        return self.storage.get_all(category_id, user_id)
    
    def get_all_by_subcategory(self, subcategory_id: UUID, user_id: UUID):
        return self.storage.get_all(subcategory_id, user_id)
    
    def get_by_id(self, transaction_id: UUID):
        return self.storage.get_by_id(transaction_id)
    
    def create(self, transaction_dto: TransactionDTO):
        if transaction_dto.type == 'incoming':
            if not self.storage.validate_funds_for_transaction(transaction_dto, transaction_dto.user.id):
                raise InsufficientFundsForTransaction('Does not have enough funds to perform the transaction.')
        
        transaction = transaction_dto.to_domain()
        transaction.create()
        final_dto = transaction_dto.to_dto(transaction)
        return self.storage.save(final_dto)

    def update(self, transaction_dto: TransactionDTO, id: UUID):
        transaction = transaction_dto.to_domain()
        transaction.update()
        final_dto = transaction_dto.to_dto(transaction)
        return self.storage.update(final_dto)
        
    def delete(self, transaction_id: int):
        self.storage.delete(transaction_id)
