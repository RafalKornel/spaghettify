#!/usr/bin/python
import re

text = []
result = ""

with open('input.txt') as _input:
    for line in _input:
        line = re.sub('//.*', ' ', line)
        text.append(line)

with open('output.txt', 'w+') as _output:
    for line in text:
        line = re.sub('\s+', ' ', line).strip()
        _output.write(line)
