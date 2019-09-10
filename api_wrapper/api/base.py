import utils
from api.http_client import HTTPClient

class Base(object):
    """Abstract base class for handling api"""

    def __init__(self):
        self.conf = utils.load_conf()        
        self.logger = utils.logger()
        self.http = HTTPClient()


    def __str__(self):
        # Override to print a readable string presentation of your object
        # below is a dynamic way of doing this without explicity constructing the string manually
        return "\n".join(
            ['{key}={value}'.format(key=key, value=value) for key,value in self.__dict__.items()]
        )
