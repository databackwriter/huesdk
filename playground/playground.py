from huesdk.huesdk import Hue

import os
BRIDGE_IP = os.getenv('HUE_BRIDGE_IP')
BRIDGE_USERNAME = os.getenv('HUE_BRIDGE_USERNAME')
hue = Hue(bridge_ip=BRIDGE_IP, username=BRIDGE_USERNAME)


groups = hue.get_groups()
print(groups)