from scapy.all import *

'''
    All:
        highest layer - summary()
        lowest layer - mysummary()
    Layers - sprintf()
        Transport layer:
            source port - sport
            destination port - dport
        IP layer:
            source ip - IP.src
            destination ip - IP.dst
        Data link layer:
            source MAC - src
            destination MAC - dst
'''

def callback(packet):
    # print(packet.summary())
    if ("TCP" or "UDP") in packet.summary():
        src_port = int(packet.sprintf("%sport%"))
        dst_port = int(packet.sprintf("%dport%"))
        src_ip = packet.sprintf("%IP.src%")
        dst_ip = packet.sprintf("%IP.dst%")
        src_mac = packet.sprintf("%src%")
        dst_mac = packet.sprintf("%dst%")
        print(src_ip, src_port, dst_ip, dst_port, src_mac, dst_mac)
        
sniff(prn=callback)