"""
Arguments using the built-in argparse module
"""
import argparse

from main import greet

parser = argparse.ArgumentParser(description='An example program')
parser.add_argument('--shout', action="store_true")
parser.add_argument('number', type=int, nargs='?', default=1)

args = parser.parse_args()

print(f'boolean {args.shout}')
print(f'number {args.number}')

# ------------------------------------------ #

name = input("What's your name? ")
greet(name, args.number, args.shout)
