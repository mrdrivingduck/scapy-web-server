from scapy.sendrecv import srp
from scapy.layers.l2 import Ether
from scapy.layers.l2 import ARP

net = "192.168.2.0/24"
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=net), timeout=1, filter="arp and arp[7] = 2", iface_hint=net)
for s,r in ans.res:
    mac = r.sprintf("%Ether.src%")
    ip = r.sprintf("%ARP.psrc%")
    print(mac, ip)