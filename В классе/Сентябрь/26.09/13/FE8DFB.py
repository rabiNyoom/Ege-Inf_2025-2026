from ipaddress import *

for m in range(33):
    net = ip_network(f'119.134.101.57/{m}', 0)
    print(net, net.netmask)

# 192