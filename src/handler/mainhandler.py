'''
    @author - mrdrivingduck
    @version - 2018.12.29
    @function - 
        Handler for root URL.
        Used only for testing.
'''

import tornado.web
from logger import serverLogger

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("GET - testing pages")

    def post(self):
        self.write("POST - testing pages")

    def prepare(self):
        serverLogger.info("MainHanlder got request")

    def on_finish(self):
        serverLogger.info("MainHanlder complete")