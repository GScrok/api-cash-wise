from rest_framework import serializers

class CardSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=True)
    card_last_four_digits = serializers.CharField(required=True)
    card_type = serializers.CharField(required=True)
    closing_day = serializers.IntegerField(required=True)
    due_day = serializers.IntegerField(required=True)
    credit_limit = serializers.FloatField(required=False)
    is_active = serializers.BooleanField(required=True)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)