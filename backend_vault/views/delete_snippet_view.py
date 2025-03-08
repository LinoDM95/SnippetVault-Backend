from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from backend_vault.models import Snippet
class DeleteItemView(APIView):
    
    def delete(self, request, id, *args, **kwargs):
        snippet = get_object_or_404(Snippet, id=id)

        if snippet.user == request.user:
            try:
                snippet.delete()
                return Response(
                    {"message": f"Snippet with ID {id} deleted."},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {"error": f"Deletion failed: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            if request.user in snippet.saved_by.all():
                snippet.saved_by.remove(request.user)
                return Response(
                    {"message": f"Snippet with ID {id} removed from your saved snippets."},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "Snippet not saved by you."},
                    status=status.HTTP_400_BAD_REQUEST
                )
