from ipaddress import *

for m in range(33):
    net = ip_network(f'220.127.169.23/{m}', 0)
    print(net, f'{net.netmask:b}')

# 19