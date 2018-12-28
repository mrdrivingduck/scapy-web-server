import tornado.web
from handler.mainhandler import MainHandler

def make_router():
    router = []
    router.append((r"/", MainHandler))
    
    return tornado.web.Application(router)