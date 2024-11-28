from rest_framework import serializers
from finance_control.serializers.categories_serializer import CategorySerializer

class SubcategorySerializer(serializers.Serializer):
    id           = serializers.UUIDField(required=False)
    category_id  = serializers.UUIDField(required=False)
    name         = serializers.CharField(required=True)
    budget_limit = serializers.FloatField(required=True)
    description  = serializers.CharField(required=False, allow_null=True, allow_blank=True)