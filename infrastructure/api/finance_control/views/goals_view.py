from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from finance_control_service.application.goals.goals_sevice import GoalService
from finance_control_service.application.goals.goals_dto import GoalDTO

from finance_control.repositories.categories_repository import CategoryRepository
from infrastructure.api.finance_control.repositories.goals_repository import GoalRepository
from infrastructure.api.finance_control.repositories.users_repository import UserRepository

from infrastructure.api.finance_control.serializers.goals_serializer import GoalSerializaer

class GoalView(APIView):
    
    repository: GoalRepository
    service: GoalService
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.repository = GoalRepository()
        self.service = GoalService(self.repository) 
    
    def get(self, request, pk=None) -> Response:        
        if pk:
            response = self.service.get_by_id(pk)
        else:
            response = self.service.get_all()
        
        return Response(GoalSerializaer(response, many=True).data, status=status.HTTP_200_OK)
    
    
    def post(self, request) -> Response:
        serializer = GoalSerializaer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        data = serializer.validated_data
        
        category_repository = CategoryRepository()
        category_id = data.get('category_id')
        category_dto = category_repository.get_by_id(category_id) if category_id else None
        
        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)
        
        data['category'] = category_dto
        data['user'] = user_dto
        
        try:
            goal_dto = GoalDTO(data)
            response = self.service.create(goal_dto)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(GoalSerializaer(response).data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None) -> Response:
        if not pk:
            return Response({'error': 'SubCategory id is required!'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        serializer = GoalSerializaer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        data = serializer.validated_data
        
        category_repository = CategoryRepository()
        category_dto = category_repository.get_by_id(data['category_id'])
        
        user_repository = UserRepository();
        user_dto = user_repository.get_by_id(request.user.id)
        
        data['id'] = pk
        data['category'] = category_dto
        data['user'] = user_dto
        
        try:
            goal_dto = GoalDTO(data)
            response = self.service.update(goal_dto, pk)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(GoalSerializaer(response).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk) -> Response:
        if not pk:
            return Response({'error': 'SubCategory id is required'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        self.service.delete(pk)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class GoalByCategoryView(APIView):
    
    repository: GoalRepository
    service: GoalService

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.repository = GoalRepository()
        self.service = GoalService(self.repository) 
    
    def get(self, request, pk):
        if not pk:
            return Response({'error': 'Category id is required!'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        response = self.service.get_all_by_category(pk)
            
        return Response(GoalSerializaer(response, many=True).data, status=status.HTTP_200_OK)
