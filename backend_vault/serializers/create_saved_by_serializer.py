from rest_framework import serializers
from backend_vault.models import Snippet

class CreateSavedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = []  # No extra fileds extended

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user
        if user in instance.saved_by.all():
            raise serializers.ValidationError("Snippet already saved")
        instance.saved_by.add(user)
        return instance
