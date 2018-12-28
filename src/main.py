import tornado.ioloop
import logging
import logging.config
import configparser
import router

def loadConfig(path):
    if not isinstance(path, str):
        raise TypeError("not a valid file path")
    conf = configparser.ConfigParser()
    if conf.read(path).__len__() == 0:
        raise FileNotFoundError("file not found")
    return conf

def getPort(conf):
    return conf.get("web", "port")

if __name__ == "__main__":
    # Loading configurations
    conf = loadConfig("conf/localDebug.ini")
    logging.config.fileConfig("conf/loggingConfig.ini")
    logger = logging.getLogger("root")

    logger.info("Initialize ending...")
    logger.info("Server listeining at:" + getPort(conf))

    # Server starting
    server = router.make_router()
    server.listen(getPort(conf))
    tornado.ioloop.IOLoop.current().start()
