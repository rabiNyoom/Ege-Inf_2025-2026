from ipaddress import *

net = ip_network('226.185.90.162/255.255.252.0', 0)

for n, ip in enumerate(net):
    if ip == IPv4Address('226.185.90.162'):
        print(n)
        break

# add * mask (poBITEovo) not change -> good)w