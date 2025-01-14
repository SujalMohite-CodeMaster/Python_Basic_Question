# Write a python program to retrive the path and name of the file currently begin executed.

import os
import sys
print(os.path.realpath(__file__))

