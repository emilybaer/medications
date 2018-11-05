import unittest
from api import PillPackAPI, APIError
from unittest.mock import patch
import json

class FakeResponse(object):
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    def json(self):
        return self.content

class TestPillPackAPI(unittest.TestCase):

    def setUp(self):
        self.pillpack_api = PillPackAPI()
        self.base = self.pillpack_api.base

    def test_get_request_success(self):
        with patch('api.requests.get') as mocked_get:
            url = self.base + 'medications/'
            fake_response = FakeResponse(200, test_response_json())
            mocked_get.return_value = fake_response
            request = self.pillpack_api.get_request(url)
            self.assertEqual(request, test_response_json())

    def test_get_request_failure(self):
        with patch('api.requests.get') as mocked_get:
            url = self.base + 'asdfasdf/'
            fake_response = FakeResponse(500, test_response_json())
            mocked_get.return_value = fake_response
            with self.assertRaises(APIError): self.pillpack_api.get_request(url)

    def test_get_medications(self):
        with patch('api.PillPackAPI.get_request') as mocked_get_request:
            url = self.base + 'medications/'
            mocked_get_request.return_value = test_response_json()
            request = self.pillpack_api.get_medications()
            mocked_get_request.assert_called_with(url=url)
            self.assertEqual(request, test_response_json())

    def test_get_medications_with_id(self):
        with patch('api.PillPackAPI.get_request') as mocked_get_request:
            id = 123
            url = self.base + 'medications/' + str(id)
            mocked_get_request.return_value = test_response_json()
            request = self.pillpack_api.get_medications(id=id)
            mocked_get_request.assert_called_with(url=url)
            self.assertEqual(request, test_response_json())

    def test_get_prescriptions(self):
        with patch('api.PillPackAPI.get_request') as mocked_get_request:
            url = self.base + 'prescriptions/'
            mocked_get_request.return_value = test_response_json()
            request = self.pillpack_api.get_prescriptions()
            
            mocked_get_request.assert_called_with(url=url)
            self.assertEqual(request, test_response_json())

    def test_get_prescriptions_with_id(self):
        with patch('api.PillPackAPI.get_request') as mocked_get_request:
            id = 123
            url = self.base + 'prescriptions/' + str(id)
            mocked_get_request.return_value = test_response_json()
            request = self.pillpack_api.get_prescriptions(id=id)
            mocked_get_request.assert_called_with(url=url)
            self.assertEqual(request, test_response_json())

def test_response_json():
    return[
        {
            'id':'564aab6f3032360003000000',
            'ndc':'000000001',
            'rxcui':'01010',
            'description':'Aspirin 10 MG',
            'generic':True,
            'active':True,
            'created_at':'2015-11-17T04:22:07.390Z',
            'updated_at':'2015-11-17T04:22:07.390Z'
        }
    ]

if __name__ == '__main__':
    unittest.main()
