import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.mark.django_db
def test_refresh_token():
    client = APIClient()
    
    # Create a test user
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    
    # Obtain refresh token
    refresh = RefreshToken.for_user(user)
    
    url = reverse('token_refresh')
    data = {
        'refresh': str(refresh),
    }
    
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert response.data['access'] is not None
