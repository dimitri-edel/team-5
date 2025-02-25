import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date, timedelta
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_listing_filtered_by_age():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    today = date.today()
    
    # Step 1: Create 5 users with profiles, who are 20 years old
    for i in range(5):
        user = User.objects.create_user(username=f'user20_{i}', email=f'user20_{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'User 20_{i}',
            birth_date=today - timedelta(days=20*365),
            country='USA',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 2: Create 7 users with profiles, who are 23 years old
    for i in range(7):
        user = User.objects.create_user(username=f'user23_{i}', email=f'user23_{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'User 23_{i}',
            birth_date=today - timedelta(days=23*365),
            country='USA',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 3: Create 6 users with profiles, who are 41 years old
    for i in range(6):
        user = User.objects.create_user(username=f'user41_{i}', email=f'user41_{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'User 41_{i}',
            birth_date=today - timedelta(days=41*365),
            country='USA',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 4: Create 8 users with profiles, who are 44 years old
    for i in range(8):
        user = User.objects.create_user(username=f'user44_{i}', email=f'user44_{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'User 44_{i}',
            birth_date=today - timedelta(days=44*365),
            country='USA',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 5: Create a test user with a profile, who is 18 years old
    test_user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    UserProfile.objects.create(
        user=test_user,
        display_name='Test User',
        birth_date=today - timedelta(days=18*365),
        country='USA',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 6: Have the test user login
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
    
    # Step 7: Have the test user list profiles using the age filter (age between 20 and 25)
    list_profiles_url = reverse('userprofile-list')
    list_response = client.get(list_profiles_url, {'age_min': 20, 'age_max': 25})
    
    # Step 8: Verify that there are 12 profiles in the response data
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 12
    
    # Step 9: Have the user list profiles using the age filter (age between 40 and 45)
    list_response = client.get(list_profiles_url, {'age_min': 40, 'age_max': 45})
    
    # Step 10: Verify that there are 14 profiles in the response data
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 14
    
    # Step 11: Have the user list profiles using the age filter (age between 15 and 19)
    list_response = client.get(list_profiles_url, {'age_min': 15, 'age_max': 19})
    
    # Step 12: Verify that there are no profiles in the response (The test user's profile must be excluded from the list)
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 0
