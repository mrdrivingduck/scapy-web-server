'''
    @author - mrdrivingduck
    @version - 2018.12.29
    @function - 
        Loading the logging configuration from file.
        Initializing the logger.
'''

import logging

# logging.config.fileConfig("conf/loggingConfig.ini")
# logger = logging.getLogger("root")
# logger.info("Logger initialization complete.")

hdr = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
hdr.setFormatter(formatter)

logger = logging.getLogger('WEB SERVER')
logger.setLevel(logging.DEBUG)
logger.addHandler(hdr)