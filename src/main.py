'''
    @author - mrdrivingduck
    @version 2018.12.30
    @function - 
        The entry of WEB server.
        Bind the port of server and start listening.
'''

import tornado.ioloop
import router
import threading
from config import Config
from logger import serverLogger
from sniffer import snifferThread
from util.ringbuffer import RingBuffer

if __name__ == "__main__":

    serverLogger.info("Initializing WEB server...")

    serverLogger.info("Loading WEB configuration.")
    conf = Config("conf/localDebugConfig.ini")
    serverLogger.info("Server will be listeining at:" + conf.getPort())

    # Sniffer starting
    buff = RingBuffer(conf.getBufferSize())
    tSniffer = threading.Thread(target=snifferThread, name="sniffer thread")
    tSniffer.start()
    tSniffer.join()

    # Server starting
    server = router.make_router()
    server.listen(conf.getPort())
    tornado.ioloop.IOLoop.current().start()
