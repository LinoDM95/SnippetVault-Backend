from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from backend_vault.models import Snippet
from backend_vault.serializers import CreateSavedBySerializer

class CreateSavedByAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, snippet_id):
        snippet = get_object_or_404(Snippet, id=snippet_id)
        # No Obj given. user_id via request and Snippet_id via url
        serializer = CreateSavedBySerializer(
            instance=snippet,
            data={}, 
            context={"request": request},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Snippet saved"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
