from ipaddress import ip_network
net = ip_network('77.180.176.14/255.255.254.0', False)

print(str(net[-2]).replace('.', ''))

# 77180177254
