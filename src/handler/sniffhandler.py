'''
    @author - mrdrivingduck
    @version - 2018.12.31
    @function - 
        handler for getting sniffed data.
'''

import tornado.web
import json
from serverglob import buff
from logger import serverLogger

class SniffHanlder(object):

    def get(self):
        arr = []
        while not buff.empty():
            pkt = buff.pop()
            arr.append(pkt)
        self.write(json.dumps(arr))

    def post(self):
        pass

    def prepare(self):
        pass

    def on_finish(self):
        pass