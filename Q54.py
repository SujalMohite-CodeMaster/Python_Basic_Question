# Write a python program to get the height and width of the console window.


import struct
import termios
import fcntl

def terminal_dimeesion():
    # use "fcntl" and "termios" to fetch terminal related information including size
    th,tw,hp,wp = struct.unpack("HHH",fcntl.ioctl(0,termios.TIOCGWINSZ,struct.pack("HHH",0,0,0)))
    # This code queries the terminal's width (columns) and height (rows).
    # It uses the 'TIOCGWINSZ' ioctl command to get window size information.

    # 1. Open file descriptor 0 (stdin).
    # 2. Call 'fcntl.ioctl' with 'TIOCGWINSZ' to fetch window size information.
    # 3. Unpack the received information into 'th' (height), 'tw' (width), 'hp' (horizontal pixel size), and 'wp' (vertical pixel size).
    return th,tw
print("Number of rows and columns :",terminal_dimeesion())