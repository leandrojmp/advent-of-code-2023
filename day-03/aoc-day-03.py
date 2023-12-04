import re
from sys import argv




with open(argv[1],'r') as input_file:
    schematic = []
    for line in input_file:
        # matches = list(re.finditer(r'(\d+)', line))
        schematic.append(line.replace("\n",""))
    print(schematic[0])
    print(schematic[-1])