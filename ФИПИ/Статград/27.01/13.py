from ipaddress import *
net = ip_network('17.234.25.1/255.255.224.0', False)

print(sum(map(int, f'{net[-1]}'.split('.'))))

# 537
