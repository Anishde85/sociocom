# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 02:00:00 2021

@author: me_so
"""
import csv
from collections import Counter

def get_recommendations(text):
    words = ["".join(k for k in word if k.isalpha() or k.isdigit()) for word in text.split()]
    words_to_exclude = ["the", "is", "in", "of", "on", "to", "with", "he", "they", "them", "it"]
    results = set()
    for word, count in Counter(words).most_common():
        if word in words_to_exclude: continue
        for result in recommendation(word):
            print(result)
            results.add(result)
        if len(results) >= 5: break
    return list(results)[:5]
    
def recommendation(key):

    with open('amazonData.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    c=0
    #print("Enter keyword:")
    #key=input()
    
    check=[1]
    
    url=[]
    
    for product in data[1:]:
        ok=0
        for j in check:
            word = list(product[j].lower().split(" "))
            if key in word:
                ok=1
                break
        if ok:
            url.append([product[18],product[15]])
            #url.append(product[1])
            c+=1
        if c==5:
            break
        
    return url