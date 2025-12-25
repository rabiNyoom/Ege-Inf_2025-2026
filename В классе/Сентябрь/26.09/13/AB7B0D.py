from ipaddress import *

for m in range(33):
    net = ip_network(f'179.57.101.43/{m}', 0)
    print(net, net.netmask)

# 192