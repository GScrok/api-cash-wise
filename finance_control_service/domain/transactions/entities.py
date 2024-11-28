from uuid import UUID
from datetime import date
from finance_control_service.domain.user.entities import User
from finance_control_service.domain.accounts.entities import Account
from finance_control_service.domain.cards.entities import Card
from finance_control_service.domain.categories.entities import Category
from finance_control_service.domain.subcategories.entities import Subcategory
from finance_control_service.domain.transactions.exceptions import *

class Transaction(object):
    id: UUID
    user: User
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

    def create(self):
        self.is_valid()

    def update(self):
        self.is_valid()

        if not self.id:
            raise TransactionUpdateRequiresExistingTransactionId('Cannot update a transaction without its Id')

    def is_valid(self):
        if self.user is None:
            raise UserTransactionCannotBeEmpty('The transaction user cannot be empty')
        if self.account_id is None:
            raise AccountTransactionCannotBeEmpty('The transaction account id cannot be empty')
        if self.category_id is None:
            raise CategoryTransactionCannotBeEmpty('The transaction category id cannot be empty')
        if self.type not in ['incoming', 'expense']:
            raise InvalidTransactionType('The transaction type must be incoming or expense')
        if self.amount <= 0:
            raise TransactionAmountMustBeGreaterThanZero('The transaction amount must be greater than zero')
        if not self.description:
            raise DescriptionTransactionCannotBeEmpty('The transaction description cannot be empty')
        if len(self.description) > 250:
            raise DescriptionTransactionCannotBeGreaterThan250Characters('The transaction description cannot be greater than 250 characters')
        if not self.transaction_date:
            raise TransactionDateCannotBeEmpty('The transaction date cannot be empty')