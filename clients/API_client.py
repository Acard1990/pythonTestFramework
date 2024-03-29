import requests
import logging

# Enable logging for requests library
logging.basicConfig(level=logging.DEBUG)

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        # note: add headers if needed

    def get(self, endpoint, **kwargs):
        url = self._full_url(endpoint)
        response = self.session.get(url, **kwargs)
        return response
    
    def post(self, endpoint, data=None, json=None, **kwargs):
        url = self._full_url(endpoint)
        response = self.session.post(url, data=data, json=json, **kwargs)
        return response
    
    def put(self, endpoint, data=None, json=None, **kwargs):
        url = self._full_url(endpoint)
        response = self.session.put(url, data=data, json=json, **kwargs)
        return response

    def patch(self, endpoint, data=None, json=None, **kwargs):
        url = self._full_url(endpoint)
        response = self.session.patch(url, data=data, json=json, **kwargs)
        return response

    def delete(self, endpoint, **kwargs):
        url = self._full_url(endpoint)
        response = self.session.delete(url, **kwargs)
        return response
    
    def _full_url(self, endpoint): 
        return self.base_url.rstrip("/") + "/" + endpoint.lstrip("/")