import unittest
import requests

class TestDeployedAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://team5-api-eu-5d24fa110c36.herokuapp.com"
    
    def test_hello_world_endpoint(self):
        """Test that the deployed /api endpoint returns Hello World"""
        response = requests.get(f"{self.base_url}/api/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "Hello, World!")

if __name__ == '__main__':
    unittest.main() 