#!/usr/bin/python
import re
from pathlib import Path

text = []
home = str(Path.home())

# Input validation
while(True):
    _path = input("Please insert path to the input file: ")
    if _path[0] == '~': _path = home + _path[1::]
    try:
        with open(_path) as test_input:
            pass
    except FileNotFoundError:
        print('This file doesn\' exists!')
    else:
        break

# Opening file and removing // comments from each line
with open(_path) as _input:
    #print(_input.read())
    for line in _input:
        line = re.sub('//.*', ' ', line)
        text.append(line)

# Creating output file, also removing white characters from each line
with open('output.txt', 'w+') as _output:
    for line in text:
        line = re.sub('\s+', ' ', line).strip()
        _output.write(line)
