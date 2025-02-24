import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_list_profiles():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create 12 users with profiles
    for i in range(12):
        user = User.objects.create_user(username=f'user{i}', email=f'user{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'User {i}',
            birth_date=date(1990, 1, 1),
            country='USA',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 2: Create a test user and his profile
    test_user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    UserProfile.objects.create(
        user=test_user,
        display_name='Test User',
        birth_date=date(1990, 1, 1),
        country='USA',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 3: Have the test user login
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
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 4: Have the test user request a list of profiles
    list_profiles_url = reverse('userprofile-list')
    list_response = client.get(list_profiles_url)
    
    # Step 5: Verify that the total number of profiles is 12
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 12
    
    # Step 6: Verify that the response contains 10 profiles on the first page
    assert len(list_response.data['results']) == 10
    
    # Step 7: Verify that the response does not contain the profile of the test user
    for profile in list_response.data['results']:
        assert profile['user'] != test_user.id
