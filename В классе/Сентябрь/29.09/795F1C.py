from ipaddress import *

for m in range(33):
    net = ip_network(f'111.81.27.224/{m}', 0)
    print(net, net.netmask)

# 192