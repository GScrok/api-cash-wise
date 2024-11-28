from dataclasses import dataclass
from uuid import UUID
from datetime import date
from finance_control_service.domain.transactions.entities import Transaction
from finance_control_service.application.user.user_dto import UserDTO

@dataclass
class TransactionDTO(object):
    id: UUID
    user: UserDTO
    account_id: UUID
    card_id: UUID | None
    category_id: UUID
    subcategory_id: UUID | None
    type: str
    amount: float
    description: str
    transaction_date: date

    def __init__(self, dict: dict):
        self.id = dict.get('id')
        self.user = dict.get('user')
        self.account_id = dict.get('account_id')
        self.card_id = dict.get('card_id')
        self.category_id = dict.get('category_id')
        self.subcategory_id = dict.get('subcategory_id')
        self.type = dict.get('type')
        self.amount = dict.get('amount')
        self.description = dict.get('description')
        self.transaction_date = dict.get('transaction_date')

    def to_domain(self):
        transaction = Transaction({
            'id': self.id,
            'user': self.user,
            'account_id': self.account_id,
            'card_id': self.card_id,
            'category_id': self.category_id,
            'subcategory_id': self.subcategory_id,
            'type': self.type,
            'amount': self.amount,
            'description': self.description,
            'transaction_date': self.transaction_date
        })
        return transaction
    
    def to_dto(self, transaction: Transaction):
        user_dto = UserDTO(transaction.user.id, transaction.user.email, 
                           transaction.user.first_name, transaction.user.last_name)

        dict = {
            'id': transaction.id,
            'user': user_dto,
            'account_id': transaction.account_id,
            'card_id': transaction.card_id,
            'category_id': transaction.category_id,
            'subcategory_id': transaction.subcategory_id,
            'type': transaction.type,
            'amount': transaction.amount,
            'description': transaction.description,
            'transaction_date': transaction.transaction_date
        }
        transaction_dto = TransactionDTO(dict)
        return transaction_dto