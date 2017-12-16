# script to read in file, replace words, and output new file
import re
# read in file

with open('./data/genderwords.txt') as gwords:
    gendered_word_list = [line.rstrip('\n') for line in gwords]

print(gendered_word_list[3])

with open('./data/Harriet.txt', 'r') as f:
    content = f.read()

    for counter in range(len(gendered_word_list)):
        print (counter)
        print(gendered_word_list[counter])
        newtxt = re.sub(gendered_word_list[counter], gendered_word_list[counter]+'ooyt ', content)
        content = newtxt
    print(content[:550])

    

#output the new text into a new file
