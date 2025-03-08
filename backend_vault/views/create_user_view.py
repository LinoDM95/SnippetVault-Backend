from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend_vault.serializers import CreateUserSerializer

class CreateUser(APIView):
  """
  View to create a user
  """
  def post(self, request):
    serializer = CreateUserSerializer(data=request.data)
    
    if serializer.is_valid():
      user = serializer.save()
      return Response({"success": True, "user-object": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
