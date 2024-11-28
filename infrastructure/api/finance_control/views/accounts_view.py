from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from infrastructure.api.finance_control.repositories.users_repository import UserRepository
from infrastructure.api.finance_control.repositories.accounts_repository import AccountRepository
from finance_control_service.application.accounts.accounts_service import AccountService
from infrastructure.api.finance_control.serializers.accounts_serializer import AccountSerializer
from finance_control_service.application.accounts.accounts_dto import AccountDTO

class AccountView(APIView):

    def get(self, request, pk = None) -> Response:
        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)
        
        repository = AccountRepository()
        service = AccountService(repository)
        
        if pk:
            response = service.get_by_id(pk)
        else:
            response = service.get_all(user_dto.id)
        
        return Response(AccountSerializer(response, many=True).data, status=status.HTTP_200_OK)
    
    def post(self, request) -> Response:
        serializer = AccountSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)
        
        data = serializer.validated_data
        data['user'] = user_dto
        
        print(data)
        
        try:
            account_dto = AccountDTO(data)
            repository = AccountRepository()
            service = AccountService(repository)
            response = service.create(account_dto)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(AccountSerializer(response).data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk) -> Response:
        if not pk:
            return Response({'error': 'Account ID is Required'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = AccountSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)
        
        data = serializer.validated_data
        data['id'] = pk
        data['user'] = user_dto
        
        try:
            account_dto = AccountDTO(data)
            repository = AccountRepository()
            service = AccountService(repository)
            response = service.update(account_dto, pk)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(AccountSerializer(response).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk) -> Response:
        if not pk:
            return Response({'error': 'Account ID is required'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        repository = AccountRepository()
        service = AccountService(repository)
        service.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)