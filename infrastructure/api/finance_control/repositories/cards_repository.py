from finance_control_service.application.cards.cards_storage import CardStorage
from finance_control_service.application.cards.cards_dto import CardDTO
from finance_control_service.application.user.user_dto import UserDTO
from finance_control.models import Card, User

from uuid import UUID

class CardRepository(CardStorage):
    def _card_dto_to_model(self, card_dto: CardDTO):
        user = User.objects.get(pk=card_dto.user.id)

        card = Card()
        card.name = card_dto.name
        card.user = user
        card.card_last_four_digits = card_dto.card_last_four_digits
        card.card_type = card_dto.card_type
        card.closing_day = card_dto.closing_day
        card.due_day = card_dto.due_day
        card.credit_limit = card_dto.credit_limit
        card.is_active = card_dto.is_active
        card.description = card_dto.description
        return card

    def _model_to_dto(self, card: Card):
        user_dto = UserDTO(card.user.id, card.user.email, card.user.first_name, card.user.last_name)

        card_dto = CardDTO(
            {
                'id': card.id,
                'name': card.name,
                'user': user_dto,
                'card_last_four_digits': card.card_last_four_digits,
                'card_type': card.card_type,
                'closing_day': card.closing_day,
                'due_day': card.due_day,
                'credit_limit': card.credit_limit,
                'is_active': card.is_active,
                'description': card.description,
            },
        )
        return card_dto

    def verify_existing_card_by_last_four_digits(self, card_dto: CardDTO) -> bool:
        existing_card = Card.objects.filter(
            card_last_four_digits=card_dto.card_last_four_digits,
            user_id=card_dto.user.id
        ).first()
        
        return existing_card is not None
    
    def verify_existing_card_by_last_four_digits_exclude_current(self, card_dto: CardDTO, pk: UUID) -> bool:
        existing_card = Card.objects.filter(
            card_last_four_digits=card_dto.card_last_four_digits,
            user_id=card_dto.user.id
        ).exclude(pk=pk).first()
        
        return existing_card is not None

    def get_by_id(self, card_id: UUID):
        card = Card.objects.get(pk=card_id)
        return self._model_to_dto(card)
    
    def get_all(self, user_id: UUID):
        cards = Card.objects.filter(user_id=user_id)
        return [self._model_to_dto(card) for card in cards]
    
    def save(self, card_dto: CardDTO):
        card = self._card_dto_to_model(card_dto)
        card.save()
        return self._model_to_dto(card)
    
    def update(self, card_dto: CardDTO):
        card = Card.objects.get(pk=card_dto.id)
        
        card.name = card_dto.name
        card.card_last_four_digits = card_dto.card_last_four_digits
        card.card_type = card_dto.card_type
        card.closing_day = card_dto.closing_day
        card.due_day = card_dto.due_day
        card.credit_limit = card_dto.credit_limit
        card.is_active = card_dto.is_active
        card.description = card_dto.description
        card.save()
        return self._model_to_dto(card)
    
    def delete(self, card_id: UUID):
        card = Card.objects.get(pk=card_id)
        card.delete()
