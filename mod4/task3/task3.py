import unittest

from mod4.task1 import app


class TestCode(unittest.TestCase):

    valid_data = {
            'email': 'pushkarev@gmail.com',
            'phone': '8888888888',
            'name': 'Andrey',
            'address': 'Lenina1',
            'index': '600343',
            'comment': 'qwe'
    }
    invalid_data = {
            'email': 'none',
            'phone': '125454547892341',
            'name': '',
            'address': '',
            'index': '454',
            'comment': 'qwe'
    }

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = '/registration'
        self.data = self.valid_data.copy()

    def test_valid_email(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        self.data['email'] = self.invalid_data['email']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('email' in response_text)

    def test_valid_phone(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone(self):
        self.data['phone'] = self.invalid_data['phone']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('phone' in response_text)

    def test_valid_name(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_name(self):
        self.data['name'] = self.invalid_data['name']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('name' in response_text)

    def test_valid_address(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_address(self):
        self.data['address'] = self.invalid_data['address']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('address' in response_text)

    def test_valid_index(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_index(self):
        self.data['index'] = self.invalid_data['index']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('index' in response_text)

if __name__ == '__main__':
    unittest.main()