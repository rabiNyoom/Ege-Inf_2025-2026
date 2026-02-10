from ipaddress import *

for m in range(33):
    net = ip_network(f'117.191.37.80/{m}', strict=False)
    print(net, net.netmask)

# 240