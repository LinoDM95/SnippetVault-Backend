import pytest
from rest_framework.test import APIClient
from rest_framework import status
from backend_vault.models import Snippet


@pytest.mark.django_db
def test_delete_existing_item():
  """
  Create a object and test a the delete api with an existing item
  
  """
  snippet = Snippet.objects.create(title="Test Snippet", language="Test Language", description="Test Description", code="Test Code")
  
  client = APIClient()
  url = f"/delete-item/{snippet.id}/"
  
  response = client.delete(url)
  
  assert response.status_code == status.HTTP_200_OK
  assert response.data["message"] == f"Item with ID {snippet.id} deleted."
  assert not Snippet.objects.filter(id=snippet.id).exists()
  
  
  @pytest.mark.django_db
  def test_delete_non_existing_item():
    """
    Search in the db for an non existing id and try to delete it
    """
    client = APIClient()
    
    max_id = Snippet.objects.all().order_by("-id").first()
    non_existent_id = (max_id.id + 1) if max_id else 1

    url = f"/delete-item/{non_existent_id}/"
    
    response = client.delete(url)
    
    assert response.status_code == status.HTTP_404_NOT_FOUND