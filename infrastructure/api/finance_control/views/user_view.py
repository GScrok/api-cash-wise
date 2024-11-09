from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from infrastructure.api.finance_control.repositories.users_repository import UserRepository
from infrastructure.api.finance_control.serializers.users_serializer import *

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
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        repository = UserRepository()
        response = repository.create_user(serializer.validated_data)
        return Response(asdict(response), status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        if not pk:
            return Response({'error': 'ID do usuário não informado'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        repository = UserRepository()
        response = repository.update_user(pk, serializer.validated_data)
        return Response(asdict(response), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if not pk:
            return Response({'error': 'ID do usuário não informado'}, status=status.HTTP_400_BAD_REQUEST)
        
        repository = UserRepository()
        repository.delete_user(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
