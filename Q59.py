# write a python program to get an absolute file path.
import os

print(os.path.abspath("wordle.pdf"))

from pathlib import Path

print(Path("Monday.docx").resolve())