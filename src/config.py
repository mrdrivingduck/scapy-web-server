'''
    @author - mrdrivingduck
    @version - 2018.12.29
    @function - 
        Loading WEB configurations from file.
        API for getting configurations.
'''

import configparser
from logger import serverLogger

def loadConfig(path):
    serverLogger.info("Loading WEB configuration.")

    if not isinstance(path, str):
        raise TypeError("not a valid file path")
    conf = configparser.ConfigParser()
    if conf.read(path).__len__() == 0:
        raise FileNotFoundError("file not found")
    return conf

conf = loadConfig("conf/localDebugConfig.ini")
# conf = loadConfig("conf/onlineConfig.ini")

def getPort():
    return conf.get("web", "port")

def getArpingTimeout():
    time_out_str = conf.get("scapy", "arping_timeout")
    return int(time_out_str)
