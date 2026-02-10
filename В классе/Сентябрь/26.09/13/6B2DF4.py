from ipaddress import *

for m in range(33):
    net = ip_network(f'117.191.176.37/{m}', 0)
    print(net, net.netmask)