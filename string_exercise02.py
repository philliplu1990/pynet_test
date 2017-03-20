#!/usr/bin/env python
ip_address = raw_input('Enter IP Address: ')
octets = ip_address.split('.')
print "{:<12}{:<12}{:<12}{:<12}".format(*octets)

for s in octets:
    print "{:>20}".format(s)


