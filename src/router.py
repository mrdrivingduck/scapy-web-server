'''
    @author - mrdrivingduck
    @version 2018.12.31
    @function - 
        Make the routing table.
        Mapping of URLs and Handlers.
'''

import tornado.web
from handler.mainhandler import MainHandler
from handler.arpinghandler import ArpingHandler
from handler.sniffhandler import SniffHanlder

def make_router():
    router = []
    router.append((r"/", MainHandler))
    router.append((r"/arping/(.*)", ArpingHandler))
    router.append((r"/sniff", SniffHanlder))
    
    return tornado.web.Application(router)