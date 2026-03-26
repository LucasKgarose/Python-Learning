# inspector/printer.py

from pprint import pprint

def pretty_print(data):
    pprint(data, indent=2, width=60)