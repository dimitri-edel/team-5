import unittest
import requests

class TestDeployedAPI(unittest.TestCase):
    def setUp(self):
        # Replace with your actual deployed URL
        self.base_url = "https://team-5-laurie-d3a9e5e7c277.herokuapp.com"
    
    def test_hello_world_endpoint(self):
        """Test that the deployed /api endpoint returns Hello World"""
        response = requests.get(f"{self.base_url}/api/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "Hello, World!")

if __name__ == '__main__':
    unittest.main() 