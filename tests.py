import unittest
from app import create_app
from config import Config

class TestConfig(Config):
    TESTING = True

class CommonTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app.testing = True
        self.app_client = self.app.test_client()

    def tearDown(self):
        pass

    def test_base_get(self):
        resp = self.app_client.get('/test')
        self.assertEqual(200, resp.status_code)
        self.assertEqual('HelloWorld!', resp.data)

if __name__ == '__main__':
    unittest.main(verbosity=2)

