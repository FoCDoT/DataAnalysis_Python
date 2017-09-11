# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 05:20:47 2017

@author: Ekansh
"""



import pandas as pd
import quandl as ql

api_key=open('api_key.txt').read()


df=ql.get('FMAC/HPI_AK', authtoken=api_key)




us_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
for abbv in us_states[0][0][1:]:
    print('FMAC/HPI_' + str(abbv))