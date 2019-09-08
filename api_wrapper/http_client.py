import requests
import json

class HTTPClient(object):
    default_header = {'Content-Type': 'application/json'}
    
    def __init__(self, ssl_verify=False):
        self.verify = ssl_verify

    def __repr__(self):
        pass

    def __str__(self):
        # Override to print a readable string presentation of your object
        # below is a dynamic way of doing this without explicity constructing the string manually
        return "\n".join(
            ['{key}={value}'.format(key=key, value=value) for key,value in self.__dict__.items()]
        )


    def _handle_response(self, res):
        """
        This is for DRY ing the response handling 
        """
        if res:
            return res.json()
        else:
            raise "Failed to get the data http error code: {}, error message: {}".format(res.status_code, res.error)


    def get(self, url, headers=None, params=None):
        res = requests.get(url, headers=headers or self.default_header, params=params, verify=self.verify)
        return self._handle_response(res)

    def put(self, method, url, params=None, data=None, headers=None, cookies=None, verify=None):
        res = None
        # requests.get()
        return res

    def post(self, method, url, params=None, data=None, headers=None, cookies=None, verify=None):
        res = None
        # requests.get()
        return res

    def delete(self, method, url, params=None, data=None, headers=None, cookies=None, verify=None):
        res = None
        # requests.get()
        return res

    def login(self):
        pass

    def logout(self):
        pass
    
    def __del__(self):
        """
        destructor we need to make sure that the session is cleared. need to do log out
        """
        self.logout()

        
        
    
    

    
    

