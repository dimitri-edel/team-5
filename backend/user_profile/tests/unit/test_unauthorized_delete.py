import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_unauthorized_delete():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create a user
    user1 = User.objects.create_user(username='user1', email='user1@example.com', password='strongpassword123')
    
    # Step 2: Create a profile for that user
    user1_profile = UserProfile.objects.create(
        user=user1,
        display_name='User One',
        birth_date=date(1990, 1, 1),
        country='USA',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 3: Have that user login
    login_url = reverse('rest_login')
    login_data = {
        'username': 'user1',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 4: Have that user attempt to delete the profile
    delete_profile_url = reverse('userprofile-detail', kwargs={'pk': user1_profile.pk})
    delete_response = client.delete(delete_profile_url)
    
    # Step 5: Verify that the deletion failed
    assert delete_response.status_code == status.HTTP_403_FORBIDDEN
    assert delete_response.data['detail'] == 'You do not have permission to perform this action.'
    
    # Step 6: Create another user
    user2 = User.objects.create_user(username='user2', email='user2@example.com', password='strongpassword123')
    
    # Step 7: Have the other user login
    login_data = {
        'username': 'user2',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 8: Have the other user attempt to delete the profile
    delete_response = client.delete(delete_profile_url)
    
    # Step 9: Verify that the deletion failed
    assert delete_response.status_code == status.HTTP_403_FORBIDDEN
    assert delete_response.data['detail'] == 'You do not have permission to perform this action.'
