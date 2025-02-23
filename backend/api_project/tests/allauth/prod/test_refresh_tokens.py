import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from api_project.tests.allauth.utils.prod_visit import visit_prod_endpoint  # Correct the import path

@pytest.mark.prod_endpoint
def test_refresh_token(visit_prod_endpoint):
    client = APIClient()
    
    # Create a test user
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    
    # Obtain refresh token
    refresh = RefreshToken.for_user(user)
    
    url = reverse('token_refresh')
    full_url = f"{visit_prod_endpoint}{url}"
    data = {
        'refresh': str(refresh),
    }
    
    response = client.post(full_url, data, format='json')
    
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert response.data['access'] is not None
