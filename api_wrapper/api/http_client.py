import requests
import json
import re

class HTTPClient(object):
    default_header = {'Content-Type': 'application/json'}
    
    def __init__(self, ssl_verify=False):
        self.verify = ssl_verify

    def __repr__(self):
        # Override to print a readable string presentation of your object
        # below is a dynamic way of doing this without explicity constructing the string manually
        return "\n".join(
            ['{key}={value}'.format(key=key, value=value) for key,value in self.__dict__.items()]
        )

    def _handle_response(self, res):
        """
        This is for DRY ing the response handling 
        """
        if res.ok:
            from pprint import pprint
            pprint(res.headers, indent=4)
            if 'Content-Type' in res.headers and re.match(r'application/json', res.headers['Content-Type'], re.IGNORECASE):
                return res.json()
            return {}
        else:
            raise Exception("Failed to make http request error: {}".format(res.status_code))

    def get(self, url, headers=None, params=None, **kwargs):
        res = requests.get(url, headers=headers or self.default_header, params=params, verify=self.verify)
        return self._handle_response(res)

    def post(self, url, headers=None, data=None, json=None, **kwargs):
        res = requests.post(url, data=data, json=json, verify=self.verify)
        return self._handle_response(res)

    def put(self, url, headers=None, data=None, json=None, **kwargs):
        res = requests.put(url, data=data, json=json, verify=self.verify)
        return self._handle_response(res)

    def delete(self, url, headers=None, params=None, data=None, json=None, **kwargs):
        res = requests.delete(url, data=data, params=None, json=json, verify=self.verify)
        return self._handle_response(res)

    def login(self):
        pass

    def logout(self):
        pass
    
    def __del__(self):
        """
        destructor we need to make sure that the session is cleared. need to do log out
        """
        self.logout()