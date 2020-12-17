# scapy-web-server

🔬 A Python WEB server using *Scapy* tools.

Created by : Mr Dk.

@2019.02.02, Ningbo, Zhejiang, China

---

## About

A WEB server based on packet manipulation tools. You can remotely invoke packet manipulation functions through HTTP by *curl*. Or maybe, a Java client program can be used for HTTP requesting - [*scapy-java-client*](https://github.com/mrdrivingduck/scapy-java-client).

## Dependency

* [Tornado](https://github.com/tornadoweb/tornado) 6.1 - A Python web framework and asynchronous networking library
* [Scapy](https://github.com/secdev/scapy) 2.4.4 - A Python-based interactive packet manipulation program & library

## Installation

*Scapy* needs root privileges to create raw sockets because it uses the Python socket library.

```bash
sudo pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
cd src
sudo python3 main.py
```

---

