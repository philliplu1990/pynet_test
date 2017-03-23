#!/usr/bin/env python
from pprint import pprint
from getpass import getpass
from pynxos.device import Device

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nexus1_ip = "nxos1.twb-tech.com"
nexus2_ip = "nxos2.twb-tech.com"
nexus3_ip = "nxos3.twb-tech.com"
nexus4_ip = "nxos4.twb-tech.com"

nexus_pair12 = [nexus1_ip, nexus2_ip]
nexus_pair34 = [nexus3_ip, nexus4_ip]



interface = 'Eth 2/4'
ip_address2 = ['192.168.5.1/24', '192.168.5.2/24']

nexus3_dict = { 'hostname': nexus3_ip, 'ip' : '192.168.5.1/24', 'peer_ip' : '192.168.5.2'}
nexus4_dict = { 'hostname': nexus4_ip, 'ip' : '192.168.5.2/24', 'peer_ip' : '192.168.5.1'}

i = 0
for switch in [nexus3_dict, nexus4_dict]:
    nxs_switch = Device(host=switch['hostname'], username="pyclass", password= '88newclass', transport='https', port=8443)
    config_int_txt = 'interface ' + interface
    config_ip_txt = 'ip address ' + switch['ip']
    config_bgp_txt = ['router bgp 10', 'neighbor {} remote-as 10'.format(switch['peer_ip']), 'address-family ipv4 unicast']
    config_list = [config_int_txt, config_ip_txt] +  config_bgp_txt
    config_interface = nxs_switch.config_list(config_list)
    

