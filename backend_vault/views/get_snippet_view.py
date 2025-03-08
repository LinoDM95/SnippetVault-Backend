from django.http import JsonResponse
from django.views import View
from backend_vault.models import Snippet

class GetSnippet(View):
    """
    Get a snippet with the id
    """
    def get(self, request, *args, **kwargs):
        id = request.GET.get('id', '')
        
        if not id:
            return JsonResponse({'error': 'No data exists'}, status=400)
        
        snippet = Snippet.objects.filter(id=id) 
        return JsonResponse({"snippet": snippet.to_dict()}, status=200)