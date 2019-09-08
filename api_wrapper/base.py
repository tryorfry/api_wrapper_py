from http_client import HTTPClient
import utils

class Base(object):
    """Abstract base class for handling the cyberark api"""

    def __init__(self):
        self.http = HTTPClient()
        self.conf = utils.load_conf()
        self.logger = utils.logger()


    def __str__(self):
        # Override to print a readable string presentation of your object
        # below is a dynamic way of doing this without explicity constructing the string manually
        return "\n".join(
            ['{key}={value}'.format(key=key, value=value) for key,value in self.__dict__.items()]
        )
        

    
    
    
