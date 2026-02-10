from ipaddress import *

net = ip_network('226.185.90.162/255.255.252.0', 0)

for n, v in enumerate(net):
    if v == ip_address('226.185.90.162'):
        print(n)
        break

# 674