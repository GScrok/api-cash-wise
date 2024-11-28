from rest_framework import serializers
from django.core.validators import MinValueValidator

class TransactionSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    account_id = serializers.UUIDField(required=True)
    card_id = serializers.UUIDField(required=False)
    category_id = serializers.UUIDField(required=True)
    subcategory_id = serializers.UUIDField(required=False)
    type = serializers.ChoiceField(choices=['incoming', 'expense'])
    amount = serializers.DecimalField(required=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = serializers.CharField(required=True)
    transaction_date = serializers.DateField(required=True)