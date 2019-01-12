'''
    @author - mrdrivingduck
    @version 2018.12.31
    @function - 
        The entry of WEB server.
        Bind the port of server and start listening.
'''

import tornado.ioloop
import router
import threading
from globall import conf
from logger import serverLogger
from sniffer import snifferThread

if __name__ == "__main__":

    serverLogger.info("Initializing WEB server...")
    serverLogger.info("Loading WEB configuration.")
    serverLogger.info("Server will be listeining at:" + conf.getPort())

    # Sniffer starting
    # tSniffer = threading.Thread(target=snifferThread, name="sniffer thread")
    # tSniffer.start()

    # Server starting
    server = router.make_router()
    server.listen(conf.getPort())
    tornado.ioloop.IOLoop.current().start()
    
    # tSniffer.join()
