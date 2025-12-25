from ipaddress import *
net = ip_network('115.198.0.0/255.254.0.0', strict=False)
c = 0
for ip in net:
    ipb = f'{ip:b}'
    if ipb.count('1') % 5 == 0:
        c += 1
print(c)
# 24786