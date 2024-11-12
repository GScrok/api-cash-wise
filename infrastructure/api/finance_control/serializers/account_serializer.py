from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=True)
    initial_balance = serializers.DecimalField(required=False)