from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from infrastructure.api.finance_control.repositories.users_repository import UserRepository
from infrastructure.api.finance_control.serializers.users_serializer import *

from finance_control.serializers.users_serializer import UserUpdateSerializer, UserCreateSerializer

class UsersView(APIView):
    def get(self, request, pk=None):
        repository = UserRepository()
        if pk:
            response = repository.get_user_by_id(pk)
        else:
            response = repository.get_all_users()

        return Response(UserUpdateSerializer(response, many=True).data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        if not pk:
            return Response({'error': 'ID do usuário não informado'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        repository = UserRepository()
        response = repository.update_user(pk, serializer.validated_data)
        return Response(UserUpdateSerializer(response).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if not pk:
            return Response({'error': 'ID do usuário não informado'}, status=status.HTTP_400_BAD_REQUEST)
        
        repository = UserRepository()
        repository.delete_user(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        repository = UserRepository()
        response = repository.create_user(serializer.validated_data)
        return Response(UserUpdateSerializer(response).data, status=status.HTTP_201_CREATED)
