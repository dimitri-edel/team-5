import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from likes.models import Like
from match.models import Match

@pytest.mark.unit
@pytest.mark.django_db
def test_list_profile_ids():
    client = APIClient(enforce_csrf_checks=False)  # Disable CSRF checks
    
    # Step 1: Create 5 users, named user1 through user5, with profiles
    profiles = []
    for i in range(1, 6):
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
    
    # Step 2: Create tester user with a profile
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
    
    # Step 3: Have user1 login
    login_url = reverse('rest_login')
    login_data = {
        'username': 'user1',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 4: Have user1 like the profile of tester user
    like_url = reverse('likeendpoint', kwargs={'pk': tester_profile.pk})  # /like/<int:pk>/
    like_response = client.post(like_url, format='json')
    assert like_response.status_code == status.HTTP_201_CREATED
    
    # Step 5: Have user1 logout
    client.credentials()  # Remove the token from the authorization header
    
    # Step 6: Have user2 login
    login_data = {
        'username': 'user2',
        'password': 'strongpassword123'
    }
    login_response = client.post(login_url, login_data, format='json')
    
    assert login_response.status_code == status.HTTP_200_OK
    assert 'key' in login_response.data
    token = login_response.data['key']
    
    # Set the token in the authorization header
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    
    # Step 7: Have user2 like the profile of tester user
    like_url = reverse('likeendpoint', kwargs={'pk': tester_profile.pk})  # /like/<int:pk>/
    like_response = client.post(like_url, format='json')
    assert like_response.status_code == status.HTTP_201_CREATED
    
    # Step 8: Have user2 logout
    client.credentials()  # Remove the token from the authorization header
    
    # Step 9: Have tester user login
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
    
    # Step 10: Have tester user like the profile of user1
    like_url = reverse('likeendpoint', kwargs={'pk': profiles[0].pk})  # /like/<int:pk>/
    like_response = client.post(like_url, format='json')
    assert like_response.status_code == status.HTTP_201_CREATED
    
    # Step 11: Have tester user like the profile of user2
    like_url = reverse('likeendpoint', kwargs={'pk': profiles[1].pk})  # /like/<int:pk>/
    like_response = client.post(like_url, format='json')
    assert like_response.status_code == status.HTTP_201_CREATED
    
    # Step 12: Have tester user request a list of ids of matched profiles
    matched_profile_ids_url = reverse('matched-profile-ids')
    matched_profile_ids_response = client.get(matched_profile_ids_url, format='json')
    
    # Step 13: Confirm that there is a list of 2 elements in the response
    assert matched_profile_ids_response.status_code == status.HTTP_200_OK
    matched_profile_ids = matched_profile_ids_response.data
    assert len(matched_profile_ids) == 2
    
    # Step 14: Confirm that the ids of the profiles in the response are the ones of user1 and user2
    assert profiles[0].pk in matched_profile_ids
    assert profiles[1].pk in matched_profile_ids
