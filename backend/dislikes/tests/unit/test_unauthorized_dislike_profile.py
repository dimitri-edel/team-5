import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from dislikes.models import Dislikes

@pytest.mark.unit
@pytest.mark.django_db
def test_unauthorized_remove_dislike_profile():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create a target user with a profile
    target_user = User.objects.create_user(username='targetuser', email='targetuser@example.com', password='strongpassword123')
    target_profile = UserProfile.objects.create(
        user=target_user,
        display_name='Target User',
        birth_date='1990-01-01',
        country='USA',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 2: Create a tester user with a profile
    tester_user = User.objects.create_user(username='testeruser', email='testeruser@example.com', password='strongpassword123')
    tester_profile = UserProfile.objects.create(
        user=tester_user,
        display_name='Tester User',
        birth_date='1990-01-01',
        country='USA',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 3: Have the tester user login
    login_url = reverse('rest_login')
    login_data = {
        'username': 'testeruser',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 4: Have the tester user dislike the profile of the target user
    dislike_url = reverse('dislikeendpoint', kwargs={'pk': target_profile.pk})  # /dislike/<int:pk>/
    dislike_response = client.post(dislike_url, format='json')
    
    # Step 5: Confirm that a dislike object has been created. Response status is 201 CREATED
    assert dislike_response.status_code == status.HTTP_201_CREATED
    
    # Step 6: Have the tester user logout
    client.credentials()  # Remove the token from the authorization header
    
    # Step 7: Have the target user login
    login_data = {
        'username': 'targetuser',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 8: Have the target user dislike their own profile
    self_dislike_url = reverse('dislikeendpoint', kwargs={'pk': target_profile.pk})  # /dislike/<int:pk>/
    self_dislike_response = client.post(self_dislike_url, format='json')
    
    # Step 9: Confirm that the access has been denied. Response status is 403. And Response message is "You cannot dislike your own profile"
    assert self_dislike_response.status_code == status.HTTP_403_FORBIDDEN
    assert self_dislike_response.data['message'] == "You cannot dislike your own profile"
