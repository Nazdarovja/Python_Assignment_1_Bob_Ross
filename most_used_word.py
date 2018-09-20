import collections
import os
from Utility.Downloader import download_as_file as downloader
from Utility.Textfile2json import convert as convert

def find_most_used_word(list_of_lines):
    wordcount = {}
    for line in list_of_lines:
        for word in line['message'].split(" ")[1:]:
            word = word.replace(".","")
            word = word.replace(",","")
            word = word.replace(":","")
            word = word.replace("\"","")
            word = word.replace("!","")
            word = word.replace("â€œ","")
            word = word.replace("â€˜","")
            word = word.replace("*","")
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(10):
        print(word, ": ", count)
