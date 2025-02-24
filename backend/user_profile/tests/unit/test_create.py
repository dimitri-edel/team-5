import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_create_user_profile():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create a user
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    
    # Step 2: Have the user login
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
 
    # Step 3: Create a new profile
    create_profile_url = reverse('userprofile-list')  # Ensure this generates the correct URL
    profile_data = {
        'user': user.id,
        'display_name': 'Test User',
        'birth_date': date(1990, 1, 1),
        'country': 'USA',
        'gender': 'M',  # Use the correct choice for gender
        'sexual_orientation': 'H',  # Use the correct choice for sexual orientation
        'city': 'Test City'
    }
    create_profile_response = client.post(create_profile_url, profile_data, format='json')
    
    # Assert successful profile creation
    assert create_profile_response.status_code == status.HTTP_201_CREATED
    assert create_profile_response.data['display_name'] == 'Test User'
    assert create_profile_response.data['birth_date'] == '1990-01-01'
    assert create_profile_response.data['country'] == 'USA'
    
    # Verify the profile is created in the database
    assert UserProfile.objects.filter(user=user).exists()
