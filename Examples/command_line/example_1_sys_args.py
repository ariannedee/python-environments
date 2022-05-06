"""
Python files can accept arguments from the command line.
  $ python file.py arg1 arg2 arg3

  The first argument is always the filename.
  All arguments are strings.
"""

import sys

from module import greet

args = sys.argv

print(f'Received {len(args)} arguments:')
for arg in args:
    print('  ' + arg)

# ------------------------------------------ #

shout = False
num = 1
for arg in args[1:]:
    if arg == '--shout':
        shout = True
    else:
        num = int(arg)

name = input("What's your name? ")
greet(name, num, shout)
