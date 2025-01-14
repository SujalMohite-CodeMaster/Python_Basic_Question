# write a pyhton program that retrives the date and time of file creation and modification.

import os.path
import time

print("File created time",time.ctime(os.path.getctime("demo.py")))
print("file modified time",time.ctime(os.path.getmtime("demo.py")))