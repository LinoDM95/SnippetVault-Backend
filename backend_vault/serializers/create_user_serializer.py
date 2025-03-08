from rest_framework import serializers
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
  '''
  Serializer to validate registration data.
  We use the standard Django User model.
  '''
  class Meta:
    model = User
    fields = ["username", "password", "email", "first_name", "last_name"]
    extra_kwargs = {
      "password": {"write_only": True}
    }
    
  def create(self, validated_data):
    return User.objects.create_user(**validated_data)