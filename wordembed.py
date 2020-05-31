# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:04:43 2020

@author: Raja
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:57:14 2020

@author: Raja
"""

from sklearn.datasets import fetch_20newsgroups
#import itertools
#import numpy as np
#import pandas as pd
from Cleaner import Cleaner

categories=["alt.atheism",
            "soc.religion.christian",
            "sci.med",
            "comp.graphics"]

cate2 = ["comp.graphics",
"comp.os.ms-windows.misc",
"comp.sys.ibm.pc.hardware",
"comp.sys.mac.hardware",
"comp.windows.x"]

twenty_train = fetch_20newsgroups(subset="train",categories=cate2, shuffle=True)
twenty_test = fetch_20newsgroups(subset="test",categories=cate2, shuffle=True)

#cleaninng data set
truck_cleaner = Cleaner()
truck_cleaner.get_data_category_count(twenty_train)
cleaner_text = truck_cleaner.text_header_remover(twenty_train.data)

#preparing dataset
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
from gensim.models import Word2Vec
from nltk.corpus import stopwords
#import numpy as np


def tokenizer_helper(cleaner_text_list):
    tokenize_sentences_list =[]
    for sentence in cleaner_text_list:
        tokenize_sentences_list.append( nltk.sent_tokenize(sentence) )
    return tokenize_sentences_list
    
def word_tokenizer(clean_tokenized_text_list):
    i=0  
    for sentences_list in clean_tokenized_text_list:
        clean_tokenized_text_list[i] = [nltk.word_tokenize(sentence) for sentence in sentences_list ]
        i = i+1
        truck_cleaner.progress_printer(len(clean_tokenized_text_list),i, "word_tokenizer" )
        
    return clean_tokenized_text_list
    
def stop_word_helper(clean_tokenized_text_list):
    for bigListIndex in range(len(clean_tokenized_text_list)):
        
        x = clean_tokenized_text_list[bigListIndex]
        for i in range (len(x)):
            x[i] = [word for word in x[i] if word not in stopwords.words('english')]
        
        clean_tokenized_text_list[bigListIndex] = x
        truck_cleaner.progress_printer(len(clean_tokenized_text_list),bigListIndex, "stop_word_helper")
    return clean_tokenized_text_list
    

clean_tokenized_text =  tokenizer_helper(cleaner_text)
clean_tokenized_text = word_tokenizer(clean_tokenized_text)
clean_tokenized_text_stop = stop_word_helper(clean_tokenized_text)


def unravel(biglist):
    ultrabiglist = []
    i=0
    for record in biglist:
        i=i+1
        print(i)
        for sentence in record:
            ultrabiglist.append(sentence)
        truck_cleaner.progress_printer(len(biglist),i, "unravel")
    
    return ultrabiglist

clean_tokenized_text_stop_unravel = unravel(clean_tokenized_text_stop)

w2v_model = Word2Vec(min_count=20,
                     window=5,
                     size=300,
                     sample=6e-5, 
                     alpha=0.03, 
                     min_alpha=0.0007, 
                     negative=2,
                     workers=4-1)

w2v_model.build_vocab(clean_tokenized_text_stop_unravel, progress_per=10000)

w2v_model.train(clean_tokenized_text_stop_unravel, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)

w2v_model.init_sims(replace=True)

w2v_model.wv.most_similar(positive=["machine"])









