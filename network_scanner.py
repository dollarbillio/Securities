#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    '''
    Ask for a MAC address based on IP address
    '''
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()

    # broadcast has a MAC address, but not definite so we use ff:ff:ff:ff:ff:ff
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast.show()

    # show what arguments are available for pdst above
    # scapy.ls(arp_result)
    arp_request_broadcast = broadcast/arp_request # / == append in scapy
    arp_request_broadcast.show()



# Call the function
scan("192.168.207.2/24")
