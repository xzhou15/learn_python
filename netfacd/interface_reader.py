#!/usr/bin/env python3

import netifaces

#interface = netifaces.interfaces()
#print(interface)

def showIP(interface):
    print('IP: ', end='')  # This print statement will always print IP without an end of line
    print((netifaces.ifaddresses(interface)[netifaces.AF_INET])[0]['addr']) # Prints the IP address

def showMAC(interface):
    print('MAC: ', end='') # This print statement will always print MAC without an end of line
    print((netifaces.ifaddresses(interface)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        showIP(i)
        showMAC(i)
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

