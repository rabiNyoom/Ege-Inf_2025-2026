from ipaddress import *

for m in range(33):
    net = ip_network(f'117.191.176.37/{m}', 0)
    
    if '117.191.160.0' in net.compressed:
        print(net, net.netmask)

# 224