#!/usr/bin/env python3
ipchk = input("Apply an IP address: ")

if ipchk == "192.168.1.1":
    print("Looks like the Ip was set to: " + ipchk + " This looks like the wrong IP")
elif ipchk:
    print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not provide input")
