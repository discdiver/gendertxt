# script to read in file, replace words, and output new file
import re
# read in file

with open('./data/Harriet.txt') as f:
    content = f.readlines()
    print(type(content))

    newlines = []

    for line in content:
        print(line)
        newline = re.sub('Harry', 'Harriet', line)
        newline = re.sub('Mrs.', 'Mrs.oo', line)
        newlines.append(newline)
    print(newlines[:50])
