from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from finance_control_service.application.categories.categories_service import CategoryService
from finance_control_service.application.categories.categories_dto import CategoryDto

from finance_control.repositories.repository_user import UserRepository
from finance_control.repositories.repository_category import CategoryRepository

from dataclasses import asdict

class CategoriesView(APIView):
    def get(self, request, pk=None):
        user_repository = UserRepository()
        user_dto = user_repository.get_user_by_id(request.user.id)
        
        repository = CategoryRepository()
        service = CategoryService(repository)

        if pk:
            response = service.get_category_by_id(pk)
            response = asdict(response)
        else:
            response = service.get_all_categories(user_dto.id)
            response = [asdict(item) for item in list(response)]


        return Response(response, status=status.HTTP_200_OK)
    
    """
    Parâmetros aceitos:
    - name: Nome da categoria
    - budget_limit: Limite de orçamento da categoria
    - description: Descrição da categoria
    """
    def post(self, request):
        name = request.data.get('name')
        budget_limit = request.data.get('budget_limit')
        description = request.data.get('description')
        
        user_repository = UserRepository()
        user_dto = user_repository.get_user_by_id(request.user.id)

        category_dto = CategoryDto(name, user_dto, budget_limit, description)
        repository = CategoryRepository()
        service = CategoryService(repository)
        response = service.create_new_category(category_dto)

        return Response(asdict(response), status=status.HTTP_201_CREATED)

    """
    Parâmetros aceitos:
    - id: ID da categoria
    - name: Nome da categoria
    - budget_limit: Limite de orçamento da categoria
    - description: Descrição da categoria
    """
    def put(self, request, pk=None):
        name = request.data.get('name')
        budget_limit = request.data.get('budget_limit')
        description = request.data.get('description')
        print(pk)
        user_repository = UserRepository()
        user_dto = user_repository.get_user_by_id(request.user.id)

        category_dto = CategoryDto(name, user_dto, pk, budget_limit, description)
        repository = CategoryRepository()
        service = CategoryService(repository)
        response = service.update_category(category_dto)
        print(response)

        return Response(asdict(response), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        repository = CategoryRepository()
        service = CategoryService(repository)
        service.delete_category(pk)

        return Response(status=status.HTTP_204_NO_CONTENT)
