from dataclasses import dataclass
from uuid import UUID
from datetime import date
from finance_control_service.domain.transactions.entities import Transaction
from finance_control_service.application.user.user_dto import UserDTO
from finance_control_service.application.cards.cards_dto import CardDTO
from finance_control_service.application.accounts.accounts_dto import AccountDTO
from finance_control_service.application.categories.categories_dto import CategoryDTO
from finance_control_service.application.subcategories.subcategories_dto import SubcategoryDTO

@dataclass
class TransactionDTO(object):
    id: UUID
    user: UserDTO
    account: AccountDTO
    card: CardDTO | None
    category: CategoryDTO
    subcategory: SubcategoryDTO | None
    type: str
    amount: float
    description: str
    transaction_date: date

    def __init__(self, dict: dict):
        self.id = dict.get('id')
        self.user = dict.get('user')
        self.account = dict.get('account')
        self.card = dict.get('card')
        self.category = dict.get('category')
        self.subcategory = dict.get('subcategory')
        self.type = dict.get('type')
        self.amount = dict.get('amount')
        self.description = dict.get('description')
        self.transaction_date = dict.get('transaction_date')

    def to_domain(self):
        transaction = Transaction({
            'id': self.id,
            'user': self.user,
            'account': self.account,
            'card': self.card,
            'category': self.category,
            'subcategory': self.subcategory,
            'type': self.type,
            'amount': self.amount,
            'description': self.description,
            'transaction_date': self.transaction_date
        })
        return transaction
    
    def to_dto(self, transaction: Transaction):
        user_dto = UserDTO(transaction.user.id, transaction.user.email, 
                           transaction.user.first_name, transaction.user.last_name)
        account_dto = AccountDTO(transaction.account)
        card_dto = CardDTO(transaction.card.__dict__) if transaction.card else None
        category_dto = CategoryDTO(transaction.category.__dict__)
        subcategory_dto = SubcategoryDTO(transaction.subcategories.__dict__) if transaction.subcategory else None

        dict = {
            'id': transaction.id,
            'user': user_dto,
            'account': account_dto,
            'card': card_dto,
            'category': category_dto,
            'subcategory': subcategory_dto,
            'type': transaction.type,
            'amount': transaction.amount,
            'description': transaction.description,
            'transaction_date': transaction.transaction_date
        }
        transaction_dto = TransactionDTO(dict)
        return transaction_dto