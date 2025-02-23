import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api_project.tests.allauth.utils.prod_visit import visit_prod_endpoint  # Correct the import path

@pytest.mark.prod_endpoint
def test_user_login(visit_prod_endpoint):
    client = APIClient()
    
    # Create a test user
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    
    url = reverse('rest_login')
    full_url = f"{visit_prod_endpoint}{url}"
    data = {
        'username': 'testuser',
        'password': 'strongpassword123'
    }
    
    response = client.post(full_url, data, format='json')
    
    assert response.status_code == status.HTTP_200_OK
    assert 'key' in response.data
    assert response.data['key'] is not None
