'''
    @author - mrdrivingduck
    @version - 2018.12.31
    @function - 
        Handler for getting sniffed data.
'''

import tornado.web
import json
from globall import buff
from logger import serverLogger

class SniffHanlder(tornado.web.RequestHandler):

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