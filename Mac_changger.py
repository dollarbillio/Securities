#!/user/bin/env python

import subprocess

subprocess.call(["ifconfig"])

interface = input("interface > ")
new_MAC = input("new_MAC > ")

subprocess.call(["ifconfig", interface, 'down'])
subprocess.call(["ifconfig", interface, 'hw', 'ether', new_MAC])
subprocess.call(["ifconfig", interface, 'up'])
subprocess.call(["ifconfig", interface])