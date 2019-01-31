"""
    @author - mrdrivingduck
    @version 2018.12.31
    @function - 
        The entry of WEB server.
        Bind the port of server and start listening.
"""

import tornado.ioloop
import router
from glob import conf
from logger import serverLogger

if __name__ == "__main__":

    serverLogger.info("Initializing WEB server...")
    serverLogger.info("Loading WEB configuration.")
    serverLogger.info("Server will be listening at:" + conf.get_port())

    # Sniffer starting
    # tSniffer = threading.Thread(target=snifferThread, name="sniffer thread")
    # tSniffer.start()

    # Server starting
    server = router.make_router()
    server.listen(conf.get_port())
    tornado.ioloop.IOLoop.current().start()
    
    # tSniffer.join()
