#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
"""
Creating command line applications using the click library
Install using $ pip install click
"""
import click

from module import greet


@click.command()
@click.argument('num', default=1)
@click.option('--shout', is_flag=True)
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(num, name, shout):
    greet(name, num, shout)

hello()
