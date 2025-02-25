import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from likes.models import Like

@pytest.mark.unit
@pytest.mark.django_db
def test_like_notifications():
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
    
    # Step 4: Have the tester user like the target user's profile
    like_url = reverse('likeendpoint', kwargs={'pk': target_profile.pk})  # /like/<int:pk>/
    like_response = client.post(like_url, format='json')
    
    # Step 5: Confirm that a like has been created. Response status code is 201 for Created.
    assert like_response.status_code == status.HTTP_201_CREATED
    
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
    
    # Step 8: Have the target user request notifications
    notifications_url = reverse('notifications')
    notifications_response = client.get(notifications_url, format='json')
    
    # Step 9: Confirm that a like object is in the response
    assert notifications_response.status_code == status.HTTP_200_OK
    notifications = notifications_response.data
    assert any(
        notification['user'] == tester_profile.pk and notification['likes'] == target_profile.pk
        for notification in notifications
    )
