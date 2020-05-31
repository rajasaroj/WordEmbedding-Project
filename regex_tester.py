# -*- coding: utf-8 -*-
"""
Created on Tue May 26 00:06:58 2020

@author: Raja
"""

import re
import numpy as np

ad = re.search("\w+\W?\w+", "abcde   fande")

#print(ad)

f = open("text.txt", "r")
fa = open("text.txt", "r")
#print(len(f.readlines()))

text = f.readlines()
c_text = fa.read()


#print(   len(c_text.splitlines()) == len(text) )
#print(   bool(re.search("(\w+)(:|-)(.*)", text[10]))    )


def end_of_loop():
    raise StopIteration



print(bool(re.search(r"(\w+)(:|-)(.*)", "Subject: Re: Diamond Stealth 24 & Windows problems!!!")))
#removed_junk_text = [sentence   for sentence in text if bool(re.search("(\w+)(:|-)(.*)", sentence)) ]

#removed_junk_text = list( sentence if bool(re.search("(\w+)(:|-)(.*)", sentence)) else end_of_loop()  for sentence in text  )
sent_list=[]
count = 0

print("lenth text: " + str(len(text)))
for sentence in text:
    #print(sentence)
    
    if bool(re.search(r"(\w+)(:|-)(.*)", sentence)) or (sentence.strip()==''):
        count = count +1
        
    else:
        break;

print("count: " + str(count))


text = text[count:]
text = " ".join(text)
#text = re.sub("([^a-zA-Z0-9\.]+)"," ",text)
#text = re.sub("(\w*)([0-9]+)(\w*)"," ",text)
#print(text)
from Cleaner import Cleaner
truck_cleaner = Cleaner()
cleaner_text =truck_cleaner.text_header_remover([c_text])
#print(cleaner_text)
print( text == cleaner_text[0])

#print(text)
#print(cleaner_text[0])


    for x in clean_tokenized_text_list:  
        for i in range (len(x)):
            x[i] = [word for word in x[i] if word not in stopwords.words('english')]
        break
        
        
        
        
#print(text)

#[ re.findall("(\w+)+", sentence) for sentence in text ]

#print(sent_list)

#print(  len(removed_junk_text)  )