import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from ..utils.dev_server import dev_server  # Import the dev_server fixture

@pytest.mark.django_db
def test_refresh_token(dev_server):
    client = APIClient()
    
    # Create a test user
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    
    # Obtain refresh token
    refresh = RefreshToken.for_user(user)
    
    url = reverse('token_refresh')
    full_url = f"{dev_server}{url}"
    data = {
        'refresh': str(refresh),
    }
    
    response = client.post(full_url, data, format='json')
    
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert response.data['access'] is not None
