# Write a python program to print to STDERR.

import sys

def eprint(*args,**kwargs):
    print(*args,file=sys.stderr,**kwargs)

eprint("Sujal","Anil","Mohite",sep="--")