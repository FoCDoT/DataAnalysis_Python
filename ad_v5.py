# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:14:01 2017

@author: Ekansh
"""

import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


api_key = open('api_key.txt','r').read()
def fifty_states():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fifty_states[0][1][1:]



def get_initial_state_data():
    states=fifty_states()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value':str(abbv)} , inplace=True)
        df[abbv]=(df[abbv]-df[abbv][0])/df[abbv][0]*100

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    main_df.plot()
    save_file=open('fifty_states_pct_change_5.pickle','wb')
    pickle.dump(main_df,save_file)
    save_file.close()

#get_initial_state_data()

HPI_data=pd.read_pickle('fifty_states_pct_change_5.pickle')
HPI_data.plot(legend=None)
plt.show()
