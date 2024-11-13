from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from finance_control_service.application.categories.categories_service import CategoryService
from finance_control_service.application.categories.categories_dto import CategoryDTO

from infrastructure.api.finance_control.repositories.users_repository import UserRepository
from finance_control.repositories.categories_repository import CategoryRepository

from infrastructure.api.finance_control.serializers.categories_serializer import CategorySerializer

class CategoriesView(APIView):
    def get(self, request, pk=None):
        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)

        repository = CategoryRepository()
        service = CategoryService(repository)

        if pk:
            response = service.get_by_id(pk)
        else:
            response = service.get_all(user_dto.id)

        return Response(CategorySerializer(response, many=True).data, status=status.HTTP_200_OK)
    
    """
    Parâmetros aceitos:
    - name: Nome da categoria
    - budget_limit: Limite de orçamento da categoria
    - description: Descrição da categoria
    """
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)

        data = serializer.validated_data
        data['user'] = user_dto

        try:
            category_dto = CategoryDTO(data)
            repository = CategoryRepository()
            service = CategoryService(repository)
            response = service.create(category_dto)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(CategorySerializer(response).data, status=status.HTTP_201_CREATED)

    """
    Parâmetros aceitos:
    - id: ID da categoria
    - name: Nome da categoria
    - budget_limit: Limite de orçamento da categoria
    - description: Descrição da categoria
    """
    def put(self, request, pk=None):
        if not pk:
            return Response({'error': 'ID da categoria não informado'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)

        data = serializer.validated_data
        data['id'] = pk
        data['user'] = user_dto

        try:    
            category_dto = CategoryDTO(data)
            repository = CategoryRepository()
            service = CategoryService(repository)
            response = service.update(category_dto, pk)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(CategorySerializer(response).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if not pk:
            return Response({'error': 'ID da categoria não informado'}, status=status.HTTP_400_BAD_REQUEST)
        
        repository = CategoryRepository()
        service = CategoryService(repository)
        service.delete(pk)

        return Response(status=status.HTTP_204_NO_CONTENT)
