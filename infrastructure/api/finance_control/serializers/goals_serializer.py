from rest_framework import serializers

class GoalSerializaer(serializers.Serializer):
    
    id          = serializers.UUIDField(required=False)
    name        = serializers.CharField(required=True)
    user_id     = serializers.UUIDField(required=False)
    category_id = serializers.UUIDField(required=False)
    value       = serializers.FloatField(required=True)
    description = serializers.CharField(required=True)
    start_at    = serializers.DateTimeField(required=True)
    end_at      = serializers.DateTimeField(required=True)
