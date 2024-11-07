from abc import ABC, abstractmethod

from finance_control_service.application.user.user_dto import UserDto

class UserStorage(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id) -> UserDto:
        pass

    @abstractmethod
    def get_all_users(self) -> list[UserDto]:
        pass
    
    @abstractmethod
    def create_user(self, username, password, email, first_name=None, last_name=None) -> UserDto:
        pass

    @abstractmethod
    def update_user(self, user_id, username=None, email=None, first_name=None, last_name=None) -> UserDto:
        pass

    @abstractmethod
    def delete_user(self, user_id) -> None:
        pass