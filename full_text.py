#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import re
import random
from collections import Counter 
file_name='PMID.txt'
df = pd.DataFrame(columns = ['PMID','Full Text'])

def parse_pmid(file_name):
    fp = open(file_name, "r")
    line = fp.readline()
    arr_pmid=[]
    while line:
        arr_pmid.append(int(line)) 
        line = fp.readline()
    

    arr_pmid = list(set(arr_pmid))
    
    print('PMID有 '+str(len(arr_pmid))+' 筆')
        
    arr_pmid.sort()
    #由小到大排
    return arr_pmid

    fp.close()


def positive(df):
    
    arr_pmid=parse_pmid(file_name)
    count=0 
    #for each 
    for pmid in arr_pmid:

        try:
            # r = requests.get('https://ncbi.nlm.nih.gov/pmc/articles/pmid/'+str(pmid)+'/')
            pmid = str(pmid)
            url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/pmid/'+(pmid.replace('\n','').replace('\r',''))
            r = requests.get(url)
            f=open(str(pmid)+'.txt', 'w')
            soup = BeautifulSoup(r.text, 'html.parser')
            full_text = str(soup)
            f.write(full_text)

            count=count+1
            print('第 '+str(count)+' 筆完成')
            second = random.uniform(1.1,2.8)
            f.close()
            time.sleep(second)

        except requests.exceptions.ConnectionError :
            print('problem in pmid:',pmid)
            


        

    print('共 '+str(count)+' 筆')

    return df

#呼叫web就好
df = positive(df)
