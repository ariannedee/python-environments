"""
print "Hello <name>", count number of times
Make greeting all uppercase if shout == True
"""


def greet(name, count=1, shout=False):
    greeting = f'Hello {name}'
    if shout:
        greeting = greeting.upper()
    for i in range(count):
        print(greeting)
