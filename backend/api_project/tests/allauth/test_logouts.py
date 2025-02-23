import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_logout():
    client = APIClient()
    
    # Create a test user
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    
    # Log in the user to obtain the authentication token
    login_url = reverse('rest_login')
    login_data = {
        'username': 'testuser',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    
    # Log out the user
    logout_url = reverse('rest_logout')
    logout_response = client.post(logout_url)
    
    assert logout_response.status_code == status.HTTP_200_OK
    assert logout_response.data == {'detail': 'Successfully logged out.'}
