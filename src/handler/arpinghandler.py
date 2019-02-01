"""
    @author - Mr Dk.
    @version - 2018.02.01
    @function -
        Use Scapy to preform an ARPING function.
        The network segment is from HTTP GET URL.
    @test -
        curl -i -X POST -H "Content-Type: application/json" -d "{ \"handler\": \"arping\", \"params\": { \"timeout\": 3, \"net\": \"192.168.1.100/24\" } }" http://localhost:8888/
        curl -i -X POST -H "Content-Type: application/json" -d "{ \"handler\": \"arping\", \"params\": { \"net\": \"192.168.1.100/24\" } }" http://localhost:8888/
        curl -i -X POST -H "Content-Type: application/json" -d "{ \"handler\": \"arping\", \"params\": { \"timeout\": 3 } }" http://localhost:8888/

    @request parameter -
        {
            'version': '1.0',
            'handler': 'arping',
            'params': {
                'timeout': xxx,
                'net': '192.168.1.100/24'
            }
        }
    @response parameter -
        @success
            {
                'version': '1.0',
                'result': [
                    {
                        'mac': 'xxx',
                        'ip': 'xxx'
                    }
                ]
            }
        @failure
            {
                'version': '1.0',
                'error': {
                    'code': 'xxx',
                    'message': 'xxx'
                }
            }
"""

from logger import serverLogger
from scapy.sendrecv import srp
from scapy.layers.l2 import Ether
from scapy.layers.l2 import ARP
from handler.abstracthandler import AbstractHandler


class ArpingHandler(AbstractHandler):

    def prepare(self):
        serverLogger.info("handler --- ARPING request")

    def on_finish(self):
        serverLogger.info("handler --- ARPING complete")

    @staticmethod
    def __writing_failure():
        return {
            'version': '1.0',
            'error': {
                'code': '-2',
                'message': 'Parameter invalid'
            }
        }

    @staticmethod
    def __writing_success(res):
        return {
            'version': '1.0',
            'result': res
        }

    def handle_get(self, handler, params):
        pass

    def handle_post(self, handler, params):
        timeout = params.get('timeout')
        net = params.get('net')

        if timeout is None or net is None:
            handler.finish(self.__writing_failure())
        else:
            ans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=net), timeout=timeout, filter="arp and arp[7] = 2",
                      iface_hint=net)
            ans = ans[0]

            arr = []
            for pair in ans.res:
                receive = pair[1]
                mac = receive.sprintf("%Ether.src%")
                ip = receive.sprintf("%ARP.psrc%")
                obj = dict(mac=mac, ip=ip)
                arr.append(obj)

            handler.finish(self.__writing_success(arr))
