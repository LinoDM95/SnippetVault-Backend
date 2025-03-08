"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
import backend_vault.views as views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("Willkommen auf der Startseite!")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path("get-snippet/", views.GetSnippet.as_view(), name="get-snippet"),
    path("get-all-snippets/", views.GetAllSnippets.as_view(), name="get-all-snippets"), # without user_id
    path("get-all-snippets/<int:id>/", views.GetAllSnippets.as_view(), name="get-all-snippets-id"), # with user_id
    path("create-snippet/", views.CreateSnippetView.as_view(), name="create-snippet"),
    path('create-saved-by/<int:snippet_id>/', views.CreateSavedByAPIView.as_view(), name='create-saved-by'),
    path('delete-item/<int:id>/', views.DeleteItemView.as_view(), name='delete-item'),
    path("update-snippet/", views.SnippetUpdateView.as_view(), name="update-snippet"),
    path("api/user/", views.GetUserData.as_view(), name="user-data"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("create-user/", views.CreateUser.as_view(), name="create-user"),
    ]
