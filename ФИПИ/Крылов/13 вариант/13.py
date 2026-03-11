from ipaddress import *
net = ip_network('252.67.33.87/255.252.0.0', strict=False)
c = 0
for ip in net:
    nb = f'{ip:b}'
    a, b = nb[:16], nb[16:]
    if a.count('1') * 2 < b.count('1'):
        c += 1
print(c)

# 17
