import csv
import re
flags = re.IGNORECASE

with open ('./data/genderwords.csv') as words:
    reader = csv.reader(words)
    mydict = {row[0]: row[1] for row in reader}

    with open('./data/Harry.txt', 'r') as f1:
        with open('./data/Harriet.txt', 'w') as f2:
            for line in f1:
                x = line
                # iterate through the dictionary on that one line making any changes necessary for individual words
                for oldword, newword in mydict.items():
                    regex_match = r'\b(%s)\s+\b'
                    reg = regex_match % oldword
                    # print (reg)
                    x = re.sub(reg, oldword+'silly ', x)
                f2.write(x)
            f2.close()
        f1.close()
        with open('./data/Harriet.txt', 'r') as f4:
            with open('./data/final.txt', 'w') as f3:
                for line2 in f4:
                    x2 = line2
                    for oldword, newword in mydict.items():
                        regex_match = r'\b(%s)\s+\b'
                        sil = oldword+'silly'
                        reg = regex_match % sil

                        x2 = re.sub(reg, newword+" ", x2)
                    f3.write(x2)
                f3.close()
            f4.close()

words.close()

#x = line.replace(" "+oldword+" ", " "+oldword+"silly")
# then  f2.write(line.replace(" "+oldword+"silly", " "+neword+" ")

'''# script to read in file, replace words, and output new file
import re
import pandas as pd
# read in file

gdf = pd.read_csv('./data/genderwords.csv')     # import list of genderedword pairs as a dataframe
print(gdf)
df = gdf.loc[:, ('froms', 'tos')]
print(df)
genderword_list = []
future_genderword_list = []

genderword_list = genderword_list.append(df.froms.values.to_list())
future_genderword_list = future_genderword_list.append(df.tos.values.to_list())

with open('./data/Harriet.txt', 'r') as f:
    content = f.read()

    for word in range(len(genderword_list)):

        print(word)
        newtxt = re.sub(word, sword+'ooyt ', content)
        content = newtxt
    print(content[:550])
# output the new text into a new file
'''
