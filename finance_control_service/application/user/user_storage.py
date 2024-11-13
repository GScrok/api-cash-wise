from abc import ABC, abstractmethod

from finance_control_service.application.user.user_dto import UserDTO

class UserStorage(ABC):
    @abstractmethod
    def get_by_id(self, user_id) -> UserDTO:
        pass

    @abstractmethod
    def get_all(self) -> list[UserDTO]:
        pass
    
    @abstractmethod
    def create(self, user_dto: UserDTO) -> UserDTO:
        pass

    @abstractmethod
    def update(self, user_dto: UserDTO) -> UserDTO:
        pass

    @abstractmethod
    def delete(self, user_id) -> None:
        pass