import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..utils.dev_server import dev_server  # Import the dev_server fixture

@pytest.mark.django_db
def test_user_registration(dev_server):
    client = APIClient()
    url = reverse('rest_register')
    full_url = f"{dev_server}{url}"
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123'
    }
    
    response = client.post(full_url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert 'key' in response.data
    assert response.data['key'] is not None
