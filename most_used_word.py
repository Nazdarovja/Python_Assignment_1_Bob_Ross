import collections
import os
from Utility.Downloader import download_as_file as downloader
from Utility.Textfile2json import convert as convert

def find_most_used_word(list_of_lines):
    wordcount = {}
    for line in list_of_lines:
        for word in line['message'].split(" "):
            word = word.replace(".","")
            word = word.replace(",","")
            word = word.replace(":","")
            word = word.replace(";","")
            word = word.replace("\"","")
            word = word.replace("\n","")
            word = word.replace("/","")
            word = word.replace("?","")
            word = word.replace("!","")
            word = word.replace("â€œ","")
            word = word.replace("â€˜","")
            word = word.replace("æ","")
            word = word.replace("ø","")
            word = word.replace("å","")
            word = word.replace("*","")
            word = word.lower()



            wordcount[word] = wordcount.get(word, 0) + 1
            # if word not in wordcount:
            #     wordcount[word] = 1
            # else:
            #     wordcount[word] += 1
    
    word_counter = collections.Counter(wordcount)
    return word_counter.most_common(1)[0]
    

