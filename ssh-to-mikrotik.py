from netmiko import ConnectHandler

mikrotik = {
    'device_type': 'mikrotik_routeros',
    'ip': '192.168.1.220',
    'username': 'admin',
    'password': 'password',
    'port': 22,  # SSH port (default: 22)
}

# Establish SSH connection
net_connect = ConnectHandler(**mikrotik)

# Send command and retrieve output
output = net_connect.send_command('interface print')
print(output)

# Disconnect from the device
net_connect.disconnect()

