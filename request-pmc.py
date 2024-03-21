# -*- coding: utf-8 -*-
import os
import requests
import time
from bs4 import BeautifulSoup


pm=[]
f2=open('PMID.txt','r')
pm=f2.readlines()
f2.close()


# erc=0
def request1(start):
    count=start
    try:
        count=start
        full_number=len(pm)
        full_number=full_number-start
        for pid in range (full_number):
            time.sleep(0.2)
            pid=pid+start
            #pid=pid+16#need to (len(pm))-16
	    temp1=''
	    temp1=str(pm[pid].replace('\n','').replace('\r',''))
	    f=open(temp1+'.txt','w')
            tol='https://www.ncbi.nlm.nih.gov/pmc/articles/pmid/'+str(pm[pid].replace('\n','').replace('\r',''))
            html=requests.get(tol)
            soup = BeautifulSoup(html.text,'html.parser')
            full_p=''
            full_p=str(soup)
            f.write(full_p)
            print('第 '+str(count)+' 筆完成'+' FBID:'+str(pm[pid])) 
            count=count+1 
            f.close()
    except:
	f.close()
	time.sleep(30)
	return request1(count)
request1(0)

