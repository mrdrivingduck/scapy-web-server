"""
    @author - Mr Dk.
    @version - 2018.12.31
    @function - 
        Global variables.
"""

import os
from config import Config
from util.ringbuffer import RingBuffer

root_dir = os.path.dirname(os.path.abspath('.'))
conf = Config(root_dir + "/conf/localDebugConfig.ini")
buff = RingBuffer(conf.get_buffer_size())
