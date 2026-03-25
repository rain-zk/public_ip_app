import unittest
from unittest.mock import patch
from src.ip_service import get_my_ip_data

class TestIPApp(unittest.TestCase):
    @patch('src.ip_service.requests.get')
    def test_api_success(self, mock_get):
        # Simulate a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "ip": "8.8.8.8",
            "city": "Mountain View"
        }

        result = get_my_ip_data()
        self.assertEqual(result["ip"], "8.8.8.8")
        self.assertEqual(result["city"], "Mountain View")

if __name__ == "__main__":
    unittest.main()
