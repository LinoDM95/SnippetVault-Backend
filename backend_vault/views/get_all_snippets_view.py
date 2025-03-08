from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from backend_vault.models import Snippet
from rest_framework.permissions import IsAuthenticated

class GetAllSnippets(View):
    """
    Get all snippets and filter by user_id if provided.
    """
    
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id", None)  

        try:
            if id:
                snippets = list(Snippet.objects.filter(
                    Q(user_id=id,) |  
                    Q(saved_by=id, is_public=True) 
                ).distinct().values())

            else:
                snippets = list(Snippet.objects.filter(
                    is_public=True
                ).values("id", "title", "language", "description", "code", "is_public", "user__username"))  
            if not snippets:
                return JsonResponse({'error': 'No snippets found'}, status=404)

            keys = list(snippets[0].keys()) if snippets else []

            return JsonResponse({"snippets": snippets, "keys": keys}, status=200)
        
        except Exception as e:
            return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)
        
        
        
        




