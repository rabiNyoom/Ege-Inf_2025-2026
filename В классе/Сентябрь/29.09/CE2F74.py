from ipaddress import *

for m in range(33):
    net = ip_network(f'208.240.112.208/{m}', 0)
    print(net, net.netmask)

# 192