from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from finance_control_service.application.transactions.transactions_service import TransactionService
from finance_control_service.application.transactions.transactions_dto import TransactionDTO

from infrastructure.api.finance_control.repositories.users_repository import UserRepository
from infrastructure.api.finance_control.repositories.transactions_repository import TransactionRepository

from infrastructure.api.finance_control.serializers.transactions_serializer import TransactionSerializer


class TransactionView(APIView):
    
    repository: TransactionRepository
    service: TransactionService
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.repository = TransactionRepository()
        self.service = TransactionService(self.repository) 
    
    def get(self, request, pk=None) -> Response:        
        if pk:
            response = self.service.get_by_id(pk)
        else:
            response = self.service.get_all()
        
        return Response(TransactionSerializer(response, many=True).data, status=status.HTTP_200_OK)
    
    
    def post(self, request) -> Response:
        serializer = TransactionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)

        data = serializer.validated_data
        data['user'] = user_dto

        try:
            transaction_dto = TransactionDTO(data)
            response = self.service.create(transaction_dto)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(TransactionSerializer(response).data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None) -> Response:
        if not pk:
            return Response({'error': 'SubCategory id is required!'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        serializer = TransactionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        data = serializer.validated_data
        data['id'] = pk
        
        try:
            transaction_dto = TransactionDTO(data)
            response = self.service.update(transaction_dto, pk)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(TransactionSerializer(response).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk) -> Response:
        if not pk:
            return Response({'error': 'SubCategory id is required'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        self.service.delete(pk)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TransactionViewByCategory(APIView):
    
    repository: TransactionRepository
    service: TransactionService
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.repository = TransactionRepository()
        self.service = TransactionService(self.repository) 
    
    def get(self, request, pk=None) -> Response:        
        if not pk:
            return Response({'error': 'Category id is required!'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)\
            
        response = self.service.get_all_by_category(pk)
        
        return Response(TransactionSerializer(response, many=True).data, status=status.HTTP_200_OK)


class TransactionViewBySubategory(APIView):
    
    repository: TransactionRepository
    service: TransactionService
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.repository = TransactionRepository()
        self.service = TransactionService(self.repository) 
    
    def get(self, request, pk=None) -> Response:        
        if not pk:
            return Response({'error': 'Subcategory id is required!'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        response = self.service.get_all_by_subcategory(pk)
        
        return Response(TransactionSerializer(response, many=True).data, status=status.HTTP_200_OK)