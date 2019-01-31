"""
    @author - Mr Dk.
    @version - 2019.02.01
    @function - 
        Handler for root URL.
        Used only for testing.
    @test - 
        curl -i -X POST -H "Content-Type: application/json" -d "{ \"handler\": \"test\" }" http://localhost:8888/
"""

from tornado.web import RequestHandler
from tornado.escape import json_decode
from logger import serverLogger
from Handler.testhandler import TestHandler

handler_map = {
    "test": TestHandler()
    # "arping": arpinghandler(),
    # "sniff": sniffhandler()
}


class MainHandler(RequestHandler):

    def get(self):
        self.write("Server is running...")

    def post(self):
        param = json_decode(self.request.body)
        handler_name = param.get('handler')
        if handler_name is None or handler_name not in handler_map:
            self.write("Handler not exist")
        else:
            handler = handler_map.get(handler_name)
            handler.handle_post(self)

    def prepare(self):
        serverLogger.info("MainHanlder got request")

    def on_finish(self):
        serverLogger.info("MainHanlder complete")
