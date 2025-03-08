from django.contrib.auth.models import User
from rest_framework import serializers
from backend_vault.models import Snippet


"""
This serializer is designed to receive a user_id (as an integer) from the request, validate it, and associate it with an existing User instance before saving the Snippet.

Ensures user_id is a valid integer.
Retrieves the corresponding User instance.
Creates a Snippet object linked to the User.
Returns validated data or raises an error if the user does not exist.


"""
class CreateSnippetSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)  

    class Meta:
        model = Snippet
        fields = ["user_id", "title", "language", "description", "code"]

    def create(self, validated_data):
        user_id = validated_data.pop("user_id")  
        try:
            user = User.objects.get(id=user_id)  
        except User.DoesNotExist:
            raise serializers.ValidationError({"user_id": "Wrong user_id"}) 
        snippet = Snippet.objects.create(user=user, **validated_data) 
        return snippet
