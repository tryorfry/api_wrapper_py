from http_client import HTTPClient
import utils
from pprint import pprint
from models.safe import Safe

logger = utils.logger()
def get_test():
    http = HTTPClient(ssl_verify=True)
    logger.info('testing')
    res = http.get('https://jsonplaceholder.typicode.com/posts')
    #pprint(res)

def get_safes():
    logger.info('testing safe')
    safe = Safe()
    
    res = safe.get_safes()
    pprint(res)
    


if __name__ == '__main__':
    get_test()
    get_safes()





