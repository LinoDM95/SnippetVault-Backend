from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from backend_vault.models import Snippet
from backend_vault.serializers import UpdateSnippetSerializer

class SnippetUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        snippet_id = request.data.get("id")
        if not snippet_id:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        snippet = get_object_or_404(Snippet, id=snippet_id)

        # Überprüfen, ob der aktuell angemeldete User der Ersteller ist
        if snippet.user != request.user:
            return Response(
                {"error": "Only the creator of the snippet can update the public status."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = UpdateSnippetSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
