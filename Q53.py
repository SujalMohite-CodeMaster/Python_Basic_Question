# Write a python program to find local IP addrsses using python's stdlib.

# Import the "scoket" module to work with network related functions.

import socket
# "socket.gethostname" use for retriveing the hostname of the system within network.
local_hostname = socket.gethostname()
print(local_hostname)
# "socket.gethostbyname_ex" use to get a list of ip address associated with the hostname.
ip_address = socket.gethostbyname_ex(local_hostname)[2]
print(ip_address)

# filter out loopback address 
filtered_ips = [ip for ip in ip_address if not ip.startswith("127.")]

first_ip = filtered_ips[:5]

print(first_ip[0])