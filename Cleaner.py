# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:16:17 2020

@author: Raja
"""
import re
import numpy as np
import sys

class Cleaner:
    def __init__(self):
        "do nothing"
    
    def text_header_remover(self, text_bunch_data):
        cleaned_text_data = []
        
        for text in text_bunch_data:
            sentences = text.splitlines()
            cleaned_sentence = self.text_header_remover_helper(sentences)
            cleaned_text_data.append(cleaned_sentence)
            
        return cleaned_text_data
            
            
            
    def text_header_remover_helper(self, sentences_list):
        count = 0
        for sentence in sentences_list:
            if bool(re.search(r"(\w+)(:|-)(.*)", sentence)) or (sentence.strip()==''):
                count = count +1
            else:
                break
            
        #print("count1: " + str(count))
        sentence_unified = " ".join(sentences_list[count:])    
        sentence_unified = re.sub("([^a-zA-Z0-9\.]+)"," ",sentence_unified)
        sentence_unified = re.sub("(\w*)([0-9]+)(\w*)"," ",sentence_unified)
        
        return sentence_unified.lower()
    
    def get_data_category_count(self,twenty_test):
        uni_ele, count = np.unique(twenty_test.target,  return_counts=True)
        for uni, cont in zip(uni_ele, count):
            print( str(twenty_test.target_names[uni]) +" : " + str(cont))
        
    def progress_printer(self,list_size, remaing_size, taskname):
        val = "Progress " + taskname.capitalize() + " remainging records: "+ str(list_size-remaing_size) + " out of Total: " + str(list_size)  
        sys.stdout.write("\r"+ val)
        sys.stdout.flush()