"""Functions for making requests to the PillPack medications API"""
import requests

class APIError(Exception):
    def __init__(self, status_code, endpoint):
        self.status_code = status_code
        self.endpoint = endpoint

    def __str__(self):
        return "Error accessing {} endpoint: {}".format( self.endpoint, self.status_code)

class PillPackAPI():
    def __init__(self):
        self.base = 'http://api-sandbox.pillpack.com/'

    def get_medications(self, id=None):
        url = self.base + 'medications/'
        if id:
            url = url + str(id)
        
        return self.get_request(url=url)

    def get_prescriptions(self, id=None):
        url = self.base + 'prescriptions/'
        if id:
            url = url + str(id)
        
        return self.get_request(url=url)

    def get_request(self, url):
        request = requests.get(
            url,
            headers={'Content-Type':'application/json'}
        )

        if request.status_code != 200:
            raise APIError(request.status_code, url)

        return request.json()
