import unittest
from src.app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_connectiion(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_data(self):
        response = self.client.get("/")
        data = response.data.decode()
        self.assertIn("Random Number:", data)

    def test_valid_data(self):
        response = self.client.get("/")
        data = response.data.decode()
        random_number = int(data.split(":")[1].strip())
        self.assertGreaterEqual(random_number, 1)
        self.assertLessEqual(random_number, 1000)


if __name__ == "__main__":
    unittest.main()
