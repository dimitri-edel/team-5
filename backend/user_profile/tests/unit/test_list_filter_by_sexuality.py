import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_list_filter_by_sexuality():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create 12 users with profiles where sexual_orientation = 'H'
    for i in range(12):
        user = User.objects.create_user(username=f'hetero_user{i}', email=f'hetero_user{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'Hetero User {i}',
            birth_date=date(1990, 1, 1),
            country='USA',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
    
    # Step 2: Create 7 users with profiles where sexual_orientation = 'G'
    for i in range(7):
        user = User.objects.create_user(username=f'gay_user{i}', email=f'gay_user{i}@example.com', password='strongpassword123')
        UserProfile.objects.create(
            user=user,
            display_name=f'Gay User {i}',
            birth_date=date(1990, 1, 1),
            country='USA',
            gender='M',
            sexual_orientation='G',
            city='Test City'
        )
    
    # Step 3: Create a test user and his profile
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
    
    # Step 4: Have the test user login
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
    
    # Step 5: Have the test user request a list of profiles where sexual_orientation = 'H' for heterosexual
    list_profiles_url = reverse('userprofile-list')
    list_response = client.get(list_profiles_url, {'sexual_orientation': 'H'})
    
    # Step 6: Verify that there are only 12 profiles in the response
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 12
    
    # Step 7: Have the test user request a list of profiles where sexual_orientation = 'G' for gay
    list_response = client.get(list_profiles_url, {'sexual_orientation': 'G'})
    
    # Step 8: Verify that there are only 7 profiles in the response
    assert list_response.status_code == status.HTTP_200_OK
    assert list_response.data['count'] == 7
