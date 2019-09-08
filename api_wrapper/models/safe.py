from base import Base
from pprint import pprint

class Safe(Base):
    """handles all safe related stuffs"""

    def get_safes(self):
        res = self.http.get('https://jsonplaceholder.typicode.com/comments', params={'postId': 1})
        return res




