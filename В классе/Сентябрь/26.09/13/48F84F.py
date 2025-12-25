from ipaddress import *

net = ip_network('98.81.154.195/255.252.0.0', 0)

print(str(net[-2]).replace('.', ''))

# 9883255254