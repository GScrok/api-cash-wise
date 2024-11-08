from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from finance_control.repositories.repository_user import UserRepository

from dataclasses import asdict

class UsersView(APIView):
    def get(self, request, pk=None):
        repository = UserRepository()
        if pk:
            response = repository.get_user_by_id(pk)
            response = asdict(response)
        else:
            response = repository.get_all_users()
            response = [asdict(item) for item in list(response)]

        return Response(response, status=status.HTTP_200_OK)

    """
    Parâmetros aceitos:
    - username: Nome de usuário
    - password: Senha do usuário
    - email: Email do usuário
    - first_name: Primeiro nome do usuário (opcional)
    - last_name: Sobrenome do usuário (opcional)
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        repository = UserRepository()
        response = repository.create_user(username, password, email, first_name, last_name)
        return Response(asdict(response), status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
    
        repository = UserRepository()
        response = repository.update_user(pk, username, email, first_name, last_name)
        return Response(asdict(response), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        repository = UserRepository()
        repository.delete_user(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
