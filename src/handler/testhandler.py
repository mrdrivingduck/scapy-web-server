"""
    @author - Mr Dk.
    @version - 2019.02.01
    @function -
        For testing.

    @request parameter -
        {
            'version': '1.0',
            'handler': 'test',
            'params': None
        }
    @response parameter -
        @success
            {
                'version': '1.0',
                'result': None
            }
        @failure
            {
                'version': '1.0',
                'error': {
                    'code': 'xxx',
                    'message': 'xxx'
                }
            }
"""

from handler.abstracthandler import AbstractHandler


class TestHandler(AbstractHandler):

    @staticmethod
    def __write_success():
        return {
            'version': '1.0',
            'result': None
        }

    def handle_get(self, handler, params):
        handler.finish(TestHandler.__write_success())

    def handle_post(self, handler, params):
        handler.finish(TestHandler.__write_success())

