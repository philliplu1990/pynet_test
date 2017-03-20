#!/usr/bin/env python
ip_address = raw_input('Enter IP Address: ')
octets = ip_address.split('.')
print "{:<12}{:<12}{:<12}{:<12}".format(octets[0],octets[1],octets[2],octets[3])

