'''
    @author - mrdrivingduck
    @version 2018.12.29
    @function - 
        The entry of WEB server.
        Bind the port of server and start listening.
'''

import tornado.ioloop
import router
from config import getPort
from logger import serverLogger

if __name__ == "__main__":

    serverLogger.info("Initializing WEB server...")
    serverLogger.info("Server will be listeining at:" + getPort())

    # Server starting
    server = router.make_router()
    server.listen(getPort())
    tornado.ioloop.IOLoop.current().start()
