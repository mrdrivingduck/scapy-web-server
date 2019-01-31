"""
    @author - mrdrivingduck
    @version - 2018.12.31
    @function - 
        Loading WEB configurations from file.
        API for getting configurations.
"""

import configparser


class Config(object):

    def __init__(self, file):
        if not isinstance(file, str):
            raise TypeError("not a valid file path")
        self.__conf = configparser.ConfigParser()
        if self.__conf.read(file).__len__() == 0:
            raise FileNotFoundError("file not found")

    '''
        @function - The port on which WEB server will be listening.
    '''
    def get_port(self):
        return self.__conf.get("web", "port")

    '''
        @function - The buffer size for packets sniffing.
    '''
    def get_buffer_size(self):
        buffer_size = self.__conf.get("web", "buffer_size")
        return int(buffer_size)

    '''
        @function - The timeout time for ARPING of Scapy tool.
    '''
    def get_arping_timeout(self):
        time_out_str = self.__conf.get("scapy", "arping_timeout")
        return int(time_out_str)

    '''
        @function - The NIC on which Scapy will be sniffing.
    '''
    def get_nic(self):
        nic = self.__conf.get("scapy", "nic")
        return nic
