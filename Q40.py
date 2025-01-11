# write the python program to detemine if a python shell is executing in 32 bit or 64 bit mode on os.
import struct
print(struct.calcsize("P")*8)