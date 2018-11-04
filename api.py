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
        """Set the base url for the API"""
        self.base = 'http://api-sandbox.pillpack.com/'

    def get_medications(self, id=None):
        """Get medications from the API. If id is not specified, gets all meds. 
        Otherwise id should be the desired medication id"""
        url = self.base + 'medications/'
        if id:
            url = url + str(id)
        
        return self.get_request(url=url)

    def get_prescriptions(self, id=None):
        """Get prescriptions from the API. If id is not specified, gets all rxs. 
        Otherwise id should be the desired rx id"""
        url = self.base + 'prescriptions/'
        if id:
            url = url + str(id)
        
        return self.get_request(url=url)

    def get_request(self, url):
        """Sets up and executes a request to the specified url"""
        request = requests.get(
            url,
            headers={'Content-Type':'application/json'}
        )

        if request.status_code != 200:
            raise APIError(request.status_code, url)

        return request.json()
