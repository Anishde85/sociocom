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
            results.add(result)
        if len(results) >= 10: break
    return list(results)[:10]
    
def recommendation(key):

    with open('flipkart.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    c=0
    #print("Enter keyword:")
    #key=input()
    
    check=[3]
    url=[]
    for product in data[1:]:
        ok=0
        for j in check:
            word = list(product[j].lower().split(" "))
            if key in word:
                ok=1
                break
        if ok:
            category=list(map(str,product[4].split(">>")))[-1][1:-2]
            images=list(map(str,product[8].split(",")))[0][2:-1]
            print(images)
            url.append((product[3], category, product[7], images, product[2]))
            #url.append(product[1])
            c+=1
        if c==10:
            break
        
    return url
