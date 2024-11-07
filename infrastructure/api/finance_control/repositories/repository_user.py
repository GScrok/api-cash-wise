from finance_control_service.application.user.user_dto import UserDTO

from ..models import User

class UserRepository:
    def _user_model_user_dto(self, user):
        return UserDTO(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )

    def get_user_by_id(self, user_id) -> UserDTO:
        try:
            user = User.objects.get(pk=user_id)
            return self._user_model_user_dto(user)
        except User.DoesNotExist:
            return None

    def get_all_users(self) -> list[UserDTO]:
        users = User.objects.all()
        return [self._user_model_user_dto(user) for user in users]
    
    def create_user(self, username, password, email, first_name=None, last_name=None) -> UserDTO:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return self._user_model_user_dto(user)

    def update_user(self, user_id, username=None, email=None, first_name=None, last_name=None) -> UserDTO:
        user = self.get_user_by_id(user_id)
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return self._user_model_user_dto(user)

    def delete_user(self, user_id) -> None:
        user = self.get_user_by_id(user_id)
        user.delete()
        return self._user_model_user_dto(user)