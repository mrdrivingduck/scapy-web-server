"""
    @author - Mr Dk.
    @version 2019.01.31
    @function - 
        Make the routing table.
        Mapping of URLs and Handlers.
"""

import tornado.web
from Handler.mainhandler import MainHandler


def make_router():
    router = [(r"/", MainHandler)]
    return tornado.web.Application(router)
