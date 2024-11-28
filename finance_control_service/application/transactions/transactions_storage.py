from abc import ABC, abstractmethod

from finance_control_service.application.transactions.transactions_dto import TransactionDTO

from uuid import UUID

class TransactionStorage(ABC):
    
    @abstractmethod
    def save(self, transaction_dto: TransactionDTO) -> TransactionDTO:
        pass
    
    @abstractmethod
    def get_all(self) -> list[TransactionDTO]:
        pass
    
    @abstractmethod
    def get_all_by_category(self, category_id: UUID) -> list[TransactionDTO]:
        pass
    
    @abstractmethod
    def get_all_by_subcategory(self, subcategory_id: UUID) -> list[TransactionDTO]:
        pass

    @abstractmethod
    def validate_funds_for_transaction(self, transaction_dto: TransactionDTO, user_id: UUID) -> bool:
        pass

    @abstractmethod
    def get_by_id(self, transaction_id: UUID) -> TransactionDTO:
        pass

    @abstractmethod
    def update(self, transaction_dto: TransactionDTO) -> TransactionDTO:
        pass

    @abstractmethod
    def delete(self, transaction_id: UUID) -> None:
        pass