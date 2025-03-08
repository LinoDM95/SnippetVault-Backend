from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend_vault.models import Snippet
from backend_vault.serializers import CreateSnippetSerializer

class CreateSnippetView(APIView):
  """
  View to create a snippet and use the serializer for model validation
  """
  
  def post(self, request):
    serializer = CreateSnippetSerializer(data=request.data)
    
    if serializer.is_valid():
      snippet = serializer.save()
      return Response({"success": True, "snippet-object": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
