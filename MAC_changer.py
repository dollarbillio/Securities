#!/user/bin/env/ python

# allow command line: python MAC_changer.py -i eth0 -m 11:23:...
#                                           --interface --mac

import subprocess
import optparse
import re
import sys


# This function is weird
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
        # inputs.interface == value added after -i
        # inputs.new_mac == value added after -m
        return inputs


# Command to run on command_line
def change_MAC(interface, new_MAC):
    subprocess.call(["ifconfig", interface, 'down'])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
    subprocess.call(["ifconfig", interface, "up"])
    # subprocess.call(["ifconfig", interface])


def getcurrentMAC(interface):
    '''
    The whole part here is to return only
    the MAC_address that we are interested
    '''
    # store ifconfig eth0 in a variable
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode(sys.stdout.encoding)
    # Show only our interested MAC_address
    MacAdressSearchResult = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if MacAdressSearchResult:
        return MacAdressSearchResult.group(0)
    else:
        # if input an interface that does not have MAC_address
        return None


# Method returns (a, tuple)
inputs = get_arguments()

# Get the current_MAC before change
old_MAC = getcurrentMAC(inputs.interface)
print ("Old MAC is " + str(old_MAC))

# Run the function with parameters = inputs.<attributes>
change_MAC(inputs.interface, inputs.new_mac)
# Get current Mac_address
current_MAC = getcurrentMAC(inputs.interface)
# Return only changed MAC_address after matched with regex
print("Changing your MAC_address...")
if old_MAC != inputs.interface:
    print ("Done! Your Current MAC_address is: " + str(current_MAC))
else:
    print ("Can't change your MAC address")









