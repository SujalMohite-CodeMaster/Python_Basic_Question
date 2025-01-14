# Write a pyhton program to determine the profiling of python programs.

# Importing the cProfile module , which providea way to profile python code
import cProfile
def sum():
    print(1+2)
    # Use cProfile to profile the sum function
cProfile.run("sum()")