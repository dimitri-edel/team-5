import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    url = reverse('rest_register')
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123'
    }
    
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert 'key' in response.data
    assert response.data['key'] is not None
