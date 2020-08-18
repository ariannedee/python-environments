"""
There are 4 types of namespaces:
- built-in
- global
- enclosing
- local
"""
import math
from random import *

pi = math.pi

print(f'Built-ins\n{dir(__builtins__)}\n')
print(f'Globals\n{globals()}\n')


def outer_function(a):
    def inner_function(b):
        a = 'Z'  # Creates a new local variable (a) that is destroyed once out of inner_function
        print(f'Inner function locals\n{locals()}\n')

    inner_function("B")
    print(f'Outer function locals\n{locals()}\n')


outer_function("A")
