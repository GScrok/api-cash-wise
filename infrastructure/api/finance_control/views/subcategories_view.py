from typing import Any
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from finance_control_service.application.subcategories.subcategories_service import SubcategoryService
from finance_control_service.application.subcategories.subcategories_dto import SubcategoryDTO

from finance_control.repositories.categories_repository import CategoryRepository
from infrastructure.api.finance_control.repositories.subcategories_repository import SubcategoryRepository

from infrastructure.api.finance_control.serializers.subcategory_serializer import SubcategorySerializer

class SubcategoryView(APIView):
    
    repository: SubcategoryRepository
    service: SubcategoryService
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.repository = SubcategoryRepository()
        self.service = SubcategoryService(self.repository) 
    
    def get(self, request, pk=None) -> Response:        
        if pk:
            response = self.service.get_by_id(pk)
        else:
            response = self.service.get_all()
            
        return Response(SubcategorySerializer(response, many=True).data, status=status.HTTP_200_OK)
    
    
    def post(self, request) -> Response:
        serializer = SubcategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        category_repository = CategoryRepository()
        category_dto = category_repository.get_by_id(request.category.id)
        
        data = serializer.validated_data
        data['category'] = category_dto
        
        try:
            subcategory_dto = SubcategoryDTO(data)
            response = self.service.create(subcategory_dto)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(SubcategorySerializer(response).data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None) -> Response:
        if not pk:
            return Response({'error': 'SubCategory id is required!'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        serializer = SubcategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        category_repository = CategoryRepository()
        category_dto = category_repository.get_by_id(request.category.id)
        
        data = serializer.validated_data
        data['id'] = pk
        data['category'] = category_dto
        
        try:
            subcategory_dto = SubcategoryDTO(data)
            response = self.service.update(subcategory_dto, pk)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(SubcategorySerializer(response).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk) -> Response:
        if not pk:
            return Response({'error': 'SubCategory id is required'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        self.service.delete(pk)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubcategoryCustomView(APIView):
    
    repository: SubcategoryRepository
    service: SubcategoryService

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.repository = SubcategoryRepository()
        self.service = SubcategoryService(self.repository) 
    
    def get_all_by_category(self, request, pk):
        response = self.service.get_all_by_category(pk)
            
        return Response(SubcategorySerializer(response, many=True).data, status=status.HTTP_200_OK)
