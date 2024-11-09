from finance_control_service.domain.cards.entities import Card
from finance_control_service.application.user.user_dto import UserDTO
from uuid import UUID
from dataclasses import dataclass

@dataclass
class CardDto(object):
    id: UUID
    name: str
    user: UserDTO
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
        self.id = dict.get('id')
        self.card_last_four_digits = dict.get('card_last_four_digits')
        self.card_type = dict.get('card_type')
        self.closing_day = dict.get('closing_day')
        self.due_day = dict.get('due_day')
        self.credit_limit = dict.get('credit_limit')
        self.is_active = dict.get('is_active')
        self.description = dict.get('description')

    def to_domain(self):
        card = Card({
            'name': self.name,
            'user': self.user,
            'id': self.id,
            'card_last_four_digits': self.card_last_four_digits,
            'card_type': self.card_type,
            'closing_day': self.closing_day,
            'due_day': self.due_day,
            'credit_limit': self.credit_limit,
            'is_active': self.is_active,
            'description': self.description
        })
        return card
    
    def to_dto(self, card: Card):
        user_dto = UserDTO(card.user.id, card.user.email, card.user.first_name, card.user.last_name)

        dict = {
            'name': card.name,
            'user': user_dto,
            'id': card.id,
            'card_last_four_digits': card.card_last_four_digits,
            'card_type': card.card_type,
            'closing_day': card.closing_day,
            'due_day': card.due_day,
            'credit_limit': card.credit_limit,
            'is_active': card.is_active,
            'description': card.description
        }
        card_dto = CardDto(dict)
        return card_dto