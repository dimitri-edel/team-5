import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_unauthorized_update():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create user albert
    albert = User.objects.create_user(username='albert', email='albert@example.com', password='strongpassword123')
    
    # Step 2: Create profile for user albert
    albert_profile = UserProfile.objects.create(
        user=albert,
        display_name='Albert',
        birth_date=date(1990, 1, 1),
        country='USA',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 3: Create user david
    david = User.objects.create_user(username='david', email='david@example.com', password='strongpassword123')
    
    # Step 4: Have user david login
    login_url = reverse('rest_login')
    login_data = {
        'username': 'david',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 5: Have user david attempt to update the profile of albert
    update_profile_url = reverse('userprofile-detail', kwargs={'pk': albert_profile.pk})
    update_data = {
        'display_name': 'Updated Albert',
        'birth_date': date(1990, 1, 1),
        'country': 'USA',
        'gender': 'M',
        'sexual_orientation': 'H',
        'city': 'Updated City'
    }
    update_response = client.put(update_profile_url, update_data, format='json')
    
    # Step 6: Verify that the attempt failed, because david is not authorized to do that
    assert update_response.status_code == status.HTTP_403_FORBIDDEN
    assert update_response.data['detail'] == 'You do not have permission to perform this action.'
