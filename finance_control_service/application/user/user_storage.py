from abc import ABC, abstractmethod

from finance_control_service.application.user.user_dto import UserDto

class UserStorage(ABC):
    @abstractmethod
    def get_by_id(self, user_id) -> UserDto:
        pass

    @abstractmethod
    def get_all(self) -> list[UserDto]:
        pass
    
    @abstractmethod
    def create(self, user_dto: UserDto) -> UserDto:
        pass

    @abstractmethod
    def update(self, user_dto: UserDto) -> UserDto:
        pass

    @abstractmethod
    def delete(self, user_id) -> None:
        pass