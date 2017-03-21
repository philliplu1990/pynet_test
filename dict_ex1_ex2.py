network_device = {'ip_addr': '1.1.1.1', 'username': 'admin', 'password': 'password', 'vendor': 'cisco',
                  'model': 'CAT4500'}

for k, v in network_device.items():
    print k, v

network_device['password'] = 'password01'
network_device['secret'] = 'secret01'

print network_device.get('device_type', 'cisco_ios')

try:
    print network_device['device_type']
except KeyError:
    print "device_type field is not found"
