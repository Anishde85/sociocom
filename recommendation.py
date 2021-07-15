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
    
    check=[1,4,10,22]
    
    url=[]
    
    for product in data[1:]:
        ok=0
        for j in check:
            if key in product[j]:
                ok=1
                break
        if ok:
            url.append([product[18],product[15]])
            c+=1
        if c==5:
            break
        
    return url