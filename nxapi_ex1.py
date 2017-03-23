#!/usr/bin/env python
from pprint import pprint
from getpass import getpass
from pynxos.device import Device

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nexus_ip = "nxos4.twb-tech.com"
nxs_test = Device(host=nexus_ip, username="pyclass", password= '88newclass',
                  transport='https', port=8443)
print 'hello'
my_facts = nxs_test.facts
pprint(nxs_test.facts)

print "show version text:"

output = nxs_test.show("show version")
print output

print 'proc_board_id ' + output['proc_board_id']


