# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import os
import re

def read_file_content(filename):
    # [assignment] Add your code here
    f = open(filename)
    file_content = f.read()
    f.close()
    return file_content


def count_words():
    text = read_file_content("story.txt")
    pattern = r'[^0-9A-Za-z ]'
    mod_string = re.sub(pattern, '', text)
    mod_string = mod_string.lower()
    text_array = mod_string.split(' ')
    unique = []
    [unique.append(x) for x in text_array if x not in unique]
    dictionary = {}
    for x in unique:
        dictionary[x] = text_array.count(x)

    # [assignment] Add your code here

    print(dictionary)
    
count_words()