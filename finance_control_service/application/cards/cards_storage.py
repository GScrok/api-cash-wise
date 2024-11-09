from abc import ABC, abstractmethod

from finance_control_service.application.cards.cards_dto import CardDto

from uuid import UUID

class CardStorage(ABC):
    @abstractmethod
    def save(self, card_dto: CardDto) -> CardDto:
        pass

    @abstractmethod
    def get_all(self, user_id: int) -> list[CardDto]:
        pass

    @abstractmethod
    def get_by_id(self, card_id: int) -> CardDto:
        pass
    
    @abstractmethod
    def verify_existing_card_by_last_four_digits(self, card_dto: CardDto) -> bool:
        pass

    @abstractmethod
    def verify_existing_card_by_last_four_digits_exclude_current(self, card_dto: CardDto, pk: UUID) -> bool:
        pass

    @abstractmethod
    def update(self, card_dto: CardDto) -> CardDto:
        pass

    @abstractmethod
    def delete(self, card_id: int) -> None:
        pass
