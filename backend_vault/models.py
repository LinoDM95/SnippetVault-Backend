from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255, null=False) 
    language = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True) 
    code = models.TextField(blank=False, null=False)  
    created_at = models.DateField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    
    saved_by = models.ManyToManyField(User, related_name="saved_snippets", blank=True)

    def __str__(self):
        return self.title
    