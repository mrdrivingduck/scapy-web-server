'''
    @author - mrdrivingduck
    @version 2018.12.29
    @function - 
        Make the routing table.
        Mapping of URLs and Handlers.
'''

import tornado.web
from handler.mainhandler import MainHandler
from handler.arpinghandler import ArpingHandler

def make_router():
    router = []
    router.append((r"/", MainHandler))
    router.append((r"/arping/(.*)", ArpingHandler))
    
    return tornado.web.Application(router)