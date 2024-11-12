from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from finance_control_service.application.cards.cards_service import CardService
from finance_control_service.application.cards.cards_dto import CardDto

from infrastructure.api.finance_control.repositories.users_repository import UserRepository
from infrastructure.api.finance_control.repositories.cards_repository import CardRepository

from infrastructure.api.finance_control.serializers.cards_serializer import CardSerializer


class CardsView(APIView):
    def get(self, request, pk=None):
        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)

        repository = CardRepository()
        service = CardService(repository)

        if pk:
            response = service.get_by_id(pk)
        else:   
            response = service.get_all(user_dto.id)

        return Response(CardSerializer(response, many=True).data, status=status.HTTP_200_OK)


    """
    Parâmetros aceitos:
    - name: Nome do cartão
    - card_last_four_digits: Últimos 4 dígitos do cartão
    - card_type: Tipo do cartão
    - closing_day: Dia do fechamento da fatura
    - due_day: Dia do vencimento da fatura
    - credit_limit: Limite de crédito (opcional)
    - is_active: Se o cartão está ativo
    - description: Descrição do cartão (opcional)
    """
    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)

        data = serializer.validated_data
        data['user'] = user_dto

        try:
            card_dto = CardDto(data)
            repository = CardRepository()
            service = CardService(repository)
            response = service.create(card_dto)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(CardSerializer(response).data, status=status.HTTP_201_CREATED)

    """
    Parâmetros aceitos:
    - id: ID do cartão
    - name: Nome do cartão
    - card_last_four_digits: Últimos 4 dígitos do cartão
    - card_type: Tipo do cartão
    - closing_day: Dia do fechamento da fatura
    - due_day: Dia do vencimento da fatura
    - credit_limit: Limite de crédito (opcional)
    - is_active: Se o cartão está ativo
    - description: Descrição do cartão (opcional)
    """
    def put(self, request, pk):
        if not pk:
            return Response({'error': 'Card ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CardSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_repository = UserRepository()
        user_dto = user_repository.get_by_id(request.user.id)

        data = serializer.validated_data
        data['id'] = pk
        data['user'] = user_dto

        try:
            card_dto = CardDto(data)
            repository = CardRepository()
            service = CardService(repository)
            response = service.update(card_dto, pk)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(CardSerializer(response).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if not pk:
            return Response({'error': 'Card ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        repository = CardRepository()
        service = CardService(repository)
        service.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
