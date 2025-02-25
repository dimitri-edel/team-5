import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_listing_filtered_by_country():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create 5 users with profiles where country='USA'
    for i in range(5):
        user = User.objects.create_user(username=f'user_usa_{i}', email=f'user_usa_{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'User USA {i}',
            birth_date=date(1990, 1, 1),
            country='USA',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 2: Create 7 users with profiles where country='UK'
    for i in range(7):
        user = User.objects.create_user(username=f'user_uk_{i}', email=f'user_uk_{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'User UK {i}',
            birth_date=date(1990, 1, 1),
            country='UK',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 3: Create 6 users with profiles where country='Germany'
    for i in range(6):
        user = User.objects.create_user(username=f'user_germany_{i}', email=f'user_germany_{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'User Germany {i}',
            birth_date=date(1990, 1, 1),
            country='Germany',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 4: Create a test user with a profile where country='UK'
    test_user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    UserProfile.objects.create(
        user=test_user,
        display_name='Test User',
        birth_date=date(1990, 1, 1),
        country='UK',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 5: Have the test user login
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
    
    # Step 6: Have the test user list profiles using the country filter (country=USA)
    list_profiles_url = reverse('userprofile-list')
    list_response = client.get(list_profiles_url, {'country': 'USA'})
    
    # Step 7: Verify that there are 5 profiles in the response data
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 5
    
    # Step 8: Have the user list profiles using the country filter (country=UK)
    list_response = client.get(list_profiles_url, {'country': 'UK'})
    
    # Step 9: Verify that there are 7 profiles in the response data and the user's profile is not amongst them
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 7
    for profile in list_response.data['results']:
        assert profile['user'] != test_user.id
    
    # Step 10: Have the user list profiles using the country filter (country=Germany)
    list_response = client.get(list_profiles_url, {'country': 'Germany'})
    
    # Step 11: Verify that there are 6 profiles in the response data
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 6
