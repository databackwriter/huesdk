from huesdk import Hue
import os
BRIDGE_IP = os.getenv('HUE_BRIDGE_IP')
BRIDGE_USERNAME = os.getenv('HUE_BRIDGE_USERNAME')
hue = Hue(bridge_ip=BRIDGE_IP, username=BRIDGE_USERNAME)

import warnings
warnings.filterwarnings("ignore")


groups = hue.get_groups()
for group in groups:
    x = hue.get_group(group.id_)
    y = hue.get_light(x.lights[0])
    y.on()

    print(group)