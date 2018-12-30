'''
    @author - mrdrivingduck
    @version - 2018.12.31
    @function - 
        The wrapper for captured packets.
'''

class PacketMessage():

    def __init__(self, src_mac, dst_mac, src_ip=None, dst_ip=None, src_port=0, dst_port=0):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
