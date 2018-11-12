#!/usr/bin/python
import re

text = []
result = ""

with open('input.txt') as _input:
    for line in _input:
        line = re.sub('//.*', ' ', line)
        text.append(line.replace('\n', ' ').expandtabs(1))

with open('output.txt', 'w+') as _output:
    for line in text:
        temp_line = ""
        for i, char in enumerate(line):
            if i == 0 or i == len(line) - 1:
                if char != ' ': temp_line += char
            else:
                if char == ' ' and ( line[i - 1] == ' ' or line[i + 1] == ' ' ):
                    pass
                else:
                    temp_line += char
        _output.write(temp_line)
