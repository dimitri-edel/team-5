from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class HelloWorldTests(APITestCase):
    def test_hello_world_endpoint(self):
        """
        Ensure we can get a hello world response from the API.
        """
        url = reverse('hello-world')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Hello, World!"}) 