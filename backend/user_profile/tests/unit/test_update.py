import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_update_user_profile():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create a user
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
    
    # Step 2: Create a profile for that user
    user_profile = UserProfile.objects.create(
        user=user,
        display_name='Test User',
        birth_date=date(1990, 1, 1),
        country='USA',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 3: Have the user login
    login_url = reverse('rest_login')
    login_data = {
        'username': 'testuser',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    print(f"Login response status: {login_response.status_code}")
    print(f"Login response data: {login_response.data}")
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Verify the token is set
    print(f"Authorization header: {client._credentials}")
    
    # Step 4: Have the user change his profile
    update_profile_url = reverse('userprofile-detail', kwargs={'pk': user_profile.pk})
    print(f"Update profile URL: {update_profile_url}")
    update_data = {
        'user': user.id,
        'display_name': 'Updated Test User',
        'birth_date': date(1990, 1, 1),
        'country': 'USA',
        'gender': 'M',
        'sexual_orientation': 'H',
        'city': 'Updated City'
    }
    update_response = client.put(update_profile_url, update_data, format='json')
    
    # Assert successful profile update
    print(f"Update response status: {update_response.status_code}")
    print(f"Update response data: {update_response.data}")
    
    assert update_response.status_code == status.HTTP_200_OK
    assert update_response.data['display_name'] == 'Updated Test User'
    assert update_response.data['city'] == 'Updated City'
    
    # Step 5: Verify that the profile has been successfully updated
    user_profile.refresh_from_db()
    print(f"Updated profile display name: {user_profile.display_name}")
    print(f"Updated profile city: {user_profile.city}")
    assert user_profile.display_name == 'Updated Test User'
    assert user_profile.city == 'Updated City'
