from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=True)
    initial_balance = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)