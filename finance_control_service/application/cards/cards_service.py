from finance_control_service.application.cards.cards_dto import CardDto
from finance_control_service.domain.cards.exceptions import *
from .cards_storage import CardStorage

from uuid import UUID

class CardService(object):
    storage: CardStorage

    def __init__(self, storage: CardStorage):
        self.storage = storage

    def get_all(self, user_id: int):
        return self.storage.get_all(user_id)
    
    def get_by_id(self, card_id: int):
        return self.storage.get_by_id(card_id)
    
    def create(self, card_dto: CardDto):
        if self.storage.verify_existing_card_by_last_four_digits(card_dto):
            raise CardAlreadyExists('A card with this last four digits already exists.')
        
        card = card_dto.to_domain()
        card.create()
        final_dto = card_dto.to_dto(card)
        return self.storage.save(final_dto)

    def update(self, card_dto: CardDto, id: UUID):
        if self.storage.verify_existing_card_by_last_four_digits_exclude_current(card_dto, id):
            raise CardAlreadyExists('A card with this last four digits already exists.')
        
        card = card_dto.to_domain()
        card.update()
        final_dto = card_dto.to_dto(card)
        return self.storage.update(final_dto)
    
    def delete(self, card_id: int):
        self.storage.delete(card_id)
