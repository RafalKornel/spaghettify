#!/usr/bin/python
import re
from pathlib import Path

text = []
home = str(Path.home())
path = ''

# Input validation
while(True):
    path = input("Please insert path to the input file: ")
    if path[0] == '~': path = home + path[1::]
    try:
        # Opening file and removing // comments from each line
        with open(path) as _input:
                for line in _input:
                    line = re.sub('//.*', ' ', line)
                    text.append(line)
    except FileNotFoundError:
        print('This file doesn\' exists!')
    else:
        break


# Creating output file, also removing white characters from each line
with open('output.txt', 'w+') as _output:
    for line in text:
        line = re.sub('\s+', ' ', line).strip()
        _output.write(line)
