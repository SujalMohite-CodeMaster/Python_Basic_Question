# Write a python program to find out the number of CPUs used.

import os 
import sys,multiprocessing

print(os.cpu_count)
print(multiprocessing.cpu_count())