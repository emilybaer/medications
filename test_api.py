import unittest
from api import PillPackAPI, APIError
from unittest.mock import patch
import json

class TestPillPackAPI(unittest.TestCase):

    def setUp(self):
        self.pillpack_api = PillPackAPI()
        self.base = self.pillpack_api.base

    def test_get_request_success(self):
        url = self.base + 'medications/'

        with patch('api.requests.get') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.json = test_response_json()

            request = self.pillpack_api.get_request(url)
            self.assertEqual(request, test_response_json())

    def test_get_request_failure(self):
        url = self.base + 'asdfasdf/'

        with patch('api.requests.get') as mocked_get:
            mocked_get.return_value.status_code = 500
            mocked_get.return_value.json = test_response_json()
            
            with self.assertRaises(APIError): self.pillpack_api.get_request(url)

    def test_get_medications(self):
        url = self.base + 'medications/'
        with patch('api.PillPackAPI.get_request') as mocked_get_request:
            mocked_get_request.return_value = test_response_json()
            request = self.pillpack_api.get_medications()
            
            mocked_get_request.assert_called_with(url=url)
            self.assertEqual(request, test_response_json())

    def test_get_medications_with_id(self):
        id = 123
        url = self.base + 'medications/' + str(id)
        with patch('api.PillPackAPI.get_request') as mocked_get_request:
            mocked_get_request.return_value = test_response_json()
            request = self.pillpack_api.get_medications(id=id)
            
            mocked_get_request.assert_called_with(url=url)
            self.assertEqual(request, test_response_json())

    def test_get_prescriptions(self):
        url = self.base + 'prescriptions/'
        with patch('api.PillPackAPI.get_request') as mocked_get_request:
            mocked_get_request.return_value = test_response_json()
            request = self.pillpack_api.get_prescriptions()
            
            mocked_get_request.assert_called_with(url=url)
            self.assertEqual(request, test_response_json())

    def test_get_prescriptions_with_id(self):
        id = 123
        url = self.base + 'prescriptions/' + str(id)
        with patch('api.PillPackAPI.get_request') as mocked_get_request:
            mocked_get_request.return_value = test_response_json()
            request = self.pillpack_api.get_prescriptions(id=id)
            
            mocked_get_request.assert_called_with(url=url)
            self.assertEqual(request, test_response_json())
    

def test_response_json():
    return json.dumps(
        [
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
    )

if __name__ == '__main__':
    unittest.main()
