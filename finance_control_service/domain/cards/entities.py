from finance_control_service.domain.user.entities import User
from uuid import UUID
from finance_control_service.domain.cards.exceptions import *

class Card(object):
    id: UUID
    name: str
    user: User
    card_last_four_digits: str
    card_type: str
    closing_day: int
    due_day: int
    credit_limit: float
    is_active: bool
    description: str

    def __init__(self, dict: dict):
        self.name = dict.get('name')
        self.user = dict.get('user')
        self.card_type = dict.get('card_type')
        self.closing_day = dict.get('closing_day')
        self.due_day = dict.get('due_day')
        self.id = dict.get('id')
        self.card_last_four_digits = dict.get('card_last_four_digits')
        self.credit_limit = dict.get('credit_limit')
        self.is_active = dict.get('is_active')
        self.description = dict.get('description')

    def create(self):
        self.is_valid()

    def update(self):
        self.is_valid()	

        if not self.id:
            raise CardUpdateRequiresExistingCardId('Cannot update a card without its Id')

    def is_valid(self):
        if self.name == '':
            raise NameCardCannotBeEmpty('The card name cannot be empty')
        if self.user is None:
            raise UserCardCannotBeEmpty('The card user cannot be empty')
        if self.card_type not in ['credit', 'debit']:
            raise InvalidCardType('The card type must be credit or debit')
        if self.card_last_four_digits is None:
            raise CardLastFourDigitsCannotBeEmpty('The card last four digits cannot be empty')
        if not self._valid_if_is_number(self.card_last_four_digits):
            raise CardLastFourDigitsMustBeNumbers('The card last four digits must be numbers')
        if self.closing_day < 1 or self.closing_day > 31:
            raise InvalidClosingDay('The closing day must be between 1 and 31')
        if self.due_day < 1 or self.due_day > 31:
            raise InvalidDueDay('The due day must be between 1 and 31')
        if self.credit_limit and self.credit_limit < 0:
            raise CreditLimitCardMustBeGreaterThanZero('The card credit limit must be greater than zero')
        if self.description and len(self.description) > 250:
            raise DescriptionCardCannotBeGreaterThan250Characters('The card description cannot be greater than 250 characters')

    def _valid_if_is_number(self, value):
        return value.isdigit()

