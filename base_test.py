# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:57:14 2020

@author: Raja
"""

from sklearn.datasets import fetch_20newsgroups
import itertools
import numpy as np
import pandas as pd


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

uni_ele, count = np.unique(twenty_test.target,  return_counts=True)


for uni, cont in zip(uni_ele, count):
    print( str(twenty_test.target_names[uni]) +" : " + str(cont))



from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

text_clf = Pipeline([ ("vect", TfidfVectorizer() ),
                      ("clf", MultinomialNB())                     
                   ])


text_clf.fit(twenty_train.data, twenty_train.target)
prediction = text_clf.predict(twenty_test.data)

from sklearn import metrics
from sklearn.metrics import accuracy_score


print('Model Accuracy: ' + str( np.mean(twenty_test.target == prediction)   ))

twenty_test_df = pd.DataFrame(twenty_test.data, columns=["data"])

twenty_test_df["target"] = pd.Series(twenty_test.target)
twenty_test_df["Prediction"] = pd.Series(prediction)
twenty_test_df["target_names"] = pd.Series((np.array(twenty_test.target_names))[twenty_test_df["target"].values])

Confused_data = twenty_test_df.loc[twenty_test_df["target"] != twenty_test_df["Prediction"]]

print(twenty_test_df.head())

#target_klass =  twenty_test.target_names[twenty_test_df["target"].values]
#print(twenty_test_df["target"].values)

#print(  )
#print(Confused_data)

#fuzzy_data = twenty_test.data[twenty_test.target != prediction]

#for x in fuzzy_data:
#    print(str(x))

#print(twenty_test.target == prediction)


#print(metrics.classification_report(twenty_test.target, prediction,  target_names=twenty_test.target_names) )

#print(metrics.confusion_matrix(twenty_test.target, prediction))



