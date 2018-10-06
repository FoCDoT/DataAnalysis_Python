# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:28:04 2017

@author: Ekansh
"""

import quandl
import pandas as pd
api_key = open('api_key.txt','r').read()
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')


for abbv in fiddy_states[0][1][1:]:
    query = "FMAC/HPI_"+str(abbv)
    df = quandl.get(query, authtoken=api_key)
    df.rename(columns={'Value':str(abbv)} , inplace=True)
    df.plot()
