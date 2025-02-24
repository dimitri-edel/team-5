import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from datetime import date
from user_profile.models import UserProfile

@pytest.mark.unit
@pytest.mark.django_db
def test_admin_delete():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create a user
    user = User.objects.create_user(username='user', email='user@example.com', password='strongpassword123')
    
    # Step 2: Create a profile for that user
    user_profile = UserProfile.objects.create(
        user=user,
        display_name='User',
        birth_date=date(1990, 1, 1),
        country='USA',
        gender='M',
        sexual_orientation='H',
        city='Test City'
    )
    
    # Step 3: Create an admin user
    admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword123')
    
    # Step 4: Have the admin user login
    login_url = reverse('rest_login')
    login_data = {
        'username': 'admin',
        'password': 'adminpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 5: Have the admin user delete the profile
    delete_profile_url = reverse('userprofile-detail', kwargs={'pk': user_profile.pk})
    delete_response = client.delete(delete_profile_url)
    
    # Step 6: Verify that the deletion was successful
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT
    assert not UserProfile.objects.filter(pk=user_profile.pk).exists()
