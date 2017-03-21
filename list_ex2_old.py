# Go back to exercise splitting on IP address
ip_address = raw_input('Enter IP Address: ')
# Convert that code to save the split as a list
 octets = ip_address.split('.')
 print octets
# Set the last octet of the list to have a ‘0’ value
 octets[-1] = u'0'
 print octets
# Convert each octet to a binary number
# Print out each octet in both decimal and binary
for s in octets:
   s = int(s)
   print type(s)
   print s
   print bin(s)

