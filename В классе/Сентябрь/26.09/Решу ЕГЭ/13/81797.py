from ipaddress import *

net = ip_network('191.128.66.83/255.192.0.0', 0)

print(str(net[-2]).replace('.', ''))

# 191191255254