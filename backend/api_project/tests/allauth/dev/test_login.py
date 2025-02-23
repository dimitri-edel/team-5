import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from ..utils.dev_server import dev_server  # Import the dev_server fixture

@pytest.mark.django_db
def test_user_login(dev_server):
    client = APIClient()
    
    # Create a test user
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    
    url = reverse('rest_login')
    full_url = f"{dev_server}{url}"
    data = {
        'username': 'testuser',
        'password': 'strongpassword123'
    }
    
    response = client.post(full_url, data, format='json')
    
    assert response.status_code == status.HTTP_200_OK
    assert 'key' in response.data
    assert response.data['key'] is not None
