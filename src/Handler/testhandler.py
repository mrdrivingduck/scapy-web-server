"""
    @author - Mr Dk.
    @version - 2019.02.01
    @function -
        For testing.
"""

from Handler.abstracthandler import AbstractHandler


class TestHandler(AbstractHandler):

    def handle_get(self, handler):
        handler.write("Test handler - get")

    def handle_post(self, handler):
        handler.write("Test handler - post")

