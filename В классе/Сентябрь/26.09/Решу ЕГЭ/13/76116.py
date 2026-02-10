from ipaddress import *

net = ip_network('205.182.128.0/255.255.192.0', 0)
c = 0

for ip in net:
    s = f'{ip:b}'[16:24]
    if s.count('0') == s.count('1'):
        c += 1

print(c)

# 5120