import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from backend.test_buttons_app.tests.utils.dev_server import dev_server
from testdata.user_data import Users
from django.test import override_settings

client = APIClient()


@override_settings(DEBUG=False)
@pytest.mark.django_db
@pytest.mark.run(order=1)
def test_register_login_logout(dev_server):
    # Pass one of the users from the imported Users list
    register_user(dev_server, user=Users[0])



@override_settings(DEBUG=False)
@pytest.mark.django_db
@pytest.mark.run(order=2)
def test_user_login(dev_server, user=Users[0]):
    # First add users to the database
    register_user(dev_server, user=user)
    login_user(dev_server, user=user)

@override_settings(DEBUG=False)
@pytest.mark.django_db
@pytest.mark.run(order=3)
def test_user_logout(dev_server, user=Users[1]):
    register_user(dev_server, user=user)
    login_reosponse_data = login_user(dev_server, user=user)
    token = login_reosponse_data["key"]
    client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
    logout_user(dev_server)

def register_user(dev_server, user):
    url = reverse("rest_register").lstrip("/")
    full_url = f"{dev_server}/{url}"
    print(f"Full URL: {full_url}")

    # Exclude the email field from the user data, as it is not required
    # for registration and will cause a server error if included
    # If included the server will try to send a confirmation email
    # which will fail in the test environment
    data = {
        "username": user["username"],
        "password1": user["password"],
        "password2": user["password"],
    }

    response = client.post(full_url, data, format="json")

    print(f"Response data: {response.data}")
    assert response.status_code == status.HTTP_201_CREATED
    assert "key" in response.data
    assert response.data["key"] is not None

def login_user(dev_server, user):
    url = reverse("rest_login").lstrip("/")
    full_url = f"{dev_server}/{url}"
    print(f"Full URL: {full_url}")

    data = {"username": user["username"], "password": user["password"]}

    response = client.post(full_url, data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert "key" in response.data
    assert response.data["key"] is not None    

    # Check the contents of cookies
    cookies = response.cookies    
    
    assert "sessionid" in cookies
    return response.data

def logout_user(dev_server):
    # Logout the user
    logout_url = reverse("rest_logout").lstrip("/")
    full_logout_url = f"{dev_server}/{logout_url}"    

    logout_response = client.post(full_logout_url, format="json")

    assert logout_response.status_code == status.HTTP_200_OK
    assert "detail" in logout_response.data
    assert logout_response.data["detail"] == "Successfully logged out."
