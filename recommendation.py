# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 02:00:00 2021

@author: me_so
"""
import csv

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
            #url.append([product[18],product[15]])
            url.append(product[1])
            c+=1
        if c==5:
            break
        
    return url