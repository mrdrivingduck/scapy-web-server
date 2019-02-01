"""
    @author - Mr Dk.
    @version - 2019.02.01
    @function - 
        handler for root URL.
        Used only for testing.
    @test - 
        curl -i -X POST -H "Content-Type: application/json" -d "{ \"handler\": \"test\", \"params\": {} }" http://localhost:8888/
    @request parameter -
        {
            'version': 'xxx',
            'handler': 'xxx',
            'params': {
                ...
            }
        }
    @response parameter -
        @success
            {
                'version': 'xxx',
                'result': {
                    ...
                }
            }
        @failure
            {
                'version': 'xxx',
                'error': {
                    'code': 'xxx',
                    'message': 'xxx'
                }
            }
"""

from tornado.web import RequestHandler
from tornado.escape import json_decode
from logger import serverLogger
from handler.testhandler import TestHandler
from handler.arpinghandler import ArpingHandler

handler_map = {
    "test": TestHandler(),
    "arping": ArpingHandler()
    # "sniff": sniffhandler()
}


class MainHandler(RequestHandler):

    def prepare(self):
        serverLogger.info("Got request")

    def on_finish(self):
        serverLogger.info("Request complete")

    @staticmethod
    def __handler_not_exist():
        return {
            'version': '1.0',
            'error': {
                'code': '-1',
                'message': 'handler not exist'
            }
        }

    @staticmethod
    def __http_method_not_match():
        return {
            'version': '1.0',
            'error': {
                'code': '-3',
                'message': 'Http method not match'
            }
        }

    @staticmethod
    def __param_not_exist():
        return {
            'version': '1.0',
            'error': {
                'code': '-4',
                'message': 'Parameter missing'
            }
        }

    def get(self):
        self.finish(MainHandler.__http_method_not_match())

    def post(self):
        param = json_decode(self.request.body)
        handler_name = param.get('handler')
        params = param.get('params')
        if handler_name is None or handler_name not in handler_map:
            self.finish(MainHandler.__handler_not_exist())
        elif params is None:
            self.finish(MainHandler.__param_not_exist())
        else:
            handler = handler_map.get(handler_name)
            handler.handle_post(self, params)

