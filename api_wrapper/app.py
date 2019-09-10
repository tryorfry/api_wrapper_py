from api.http_client import HTTPClient
import utils
from pprint import pprint
from api.safe import Safe


if __name__ == '__main__':
    logger = utils.logger()
    safe = Safe()
    s = safe.get_safes()
    pprint(s)
    created = safe.post_safes()
    pprint(created, indent=8)







