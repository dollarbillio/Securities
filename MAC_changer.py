#!/user/bin/env/ python

# allow command line: python MAC_changer.py -i eth0 -m 11:23:...
#                                           --interface --mac

import subprocess
import optparse

def get_arguments():
    # Create an instance of class OptionParser
    parser = optparse.OptionParser()

    # Use a method to allow arguments to be allowed in terminal
    # (dest='') becomes an attribute of [inputs] below
    parser.add_option('-i', '--interface', dest='interface', help="Interface to change" )
    parser.add_option('-m', '--n_mac', dest='new_mac', help="Change MAC address")
    (inputs, arguments) = parser.parse_args()
    # Check if the user hasn't provided enough arguments
    if not inputs.interface:
        parser.error('[-] Please specify an interface, use --help for more info')
    elif not inputs.new_mac:
        parser.error('[-] Please specify a new_mac, use --help for more info')
    else:
        return inputs
# Command to run on command_line
def change_MAC(interface, new_MAC):
    subprocess.call(["ifconfig", interface, 'down'])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])

# Method returns (a, tuple)
inputs = get_arguments()

# Run the function with parameters = inputs.<attributes>
change_MAC(inputs.interface, inputs.new_mac)





