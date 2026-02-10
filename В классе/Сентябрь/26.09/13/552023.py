from ipaddress import *

net = ip_network('172.16.128.0/255.255.192.0', 0)
c = 0
for a in net:
    a = f'{a:b}'
    if a.count('1') % 2 == 1:
        c += 1
print(c)