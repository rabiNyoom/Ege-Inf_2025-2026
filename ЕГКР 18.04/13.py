from ipaddress import *
net = ip_network('191.89.109.206/255.255.224.0', strict=False)
ip = net[-2]
print(sum(map(int, str(ip).split('.'))))
