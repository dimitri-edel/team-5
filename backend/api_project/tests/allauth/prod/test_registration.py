import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api_project.tests.allauth.utils.prod_visit import visit_prod_endpoint  # Correct the import path

@pytest.mark.prod_endpoint
def test_user_registration(visit_prod_endpoint):
    client = APIClient()
    url = reverse('rest_register')
    full_url = f"{visit_prod_endpoint}{url}"
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
