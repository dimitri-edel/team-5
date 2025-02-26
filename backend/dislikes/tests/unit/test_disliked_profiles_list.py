import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from dislikes.models import Dislikes

@pytest.mark.unit
@pytest.mark.django_db
def test_disliked_profiles_list():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create 15 users with profiles
    profiles = []
    for i in range(15):
        user = User.objects.create_user(username=f'user{i}', email=f'user{i}@example.com', password='strongpassword123')
        profile = UserProfile.objects.create(
            user=user,
            display_name=f'User {i}',
            birth_date='1990-01-01',
            country='USA',
            gender='M',
            sexual_orientation='H',
            city='Test City'
        )
        profiles.append(profile)
    
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
    
    # Step 4: Have the tester user dislike 5 of the 15 available profiles
    for profile in profiles[:5]:
        dislike_url = reverse('dislikeendpoint', kwargs={'pk': profile.pk})  # /dislike/<int:pk>/
        dislike_response = client.post(dislike_url, format='json')
        assert dislike_response.status_code == status.HTTP_201_CREATED
    
    # Step 5: Have the tester user request a list of disliked profiles
    disliked_profiles_url = reverse('disliked-profiles')
    disliked_profiles_response = client.get(disliked_profiles_url, format='json')
    
    # Step 6: Confirm that there is a list of 5 numbers (primary keys) in the response
    assert disliked_profiles_response.status_code == status.HTTP_200_OK
    disliked_profiles = disliked_profiles_response.data
    assert len(disliked_profiles) == 5
    assert all(profile.pk in disliked_profiles for profile in profiles[:5])
