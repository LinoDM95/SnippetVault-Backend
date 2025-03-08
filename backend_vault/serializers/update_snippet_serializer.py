from rest_framework import serializers
from backend_vault.models import Snippet


class UpdateSnippetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Snippet
    fields = ['id', 'title', 'language', 'description', 'code', "is_public"]