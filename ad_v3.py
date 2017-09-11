# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:16:57 2017

@author: Ekansh
"""

import quandl
import pandas as pd
import pickle



api_key = open('api_key.txt','r').read()
def fifty_states():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fifty_states[0][0][1:]



def get_initial_state_data():
    states=fifty_states()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value':str(abbv)} , inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    main_df.plot()
    save_file=open('fifty_states.pickle','wb')
    pickle.dump(main_df,save_file)
    save_file.close()

# using pickle of python
saved_file=open('fifty_states.pickle','rb')
HPI_data=pickle.load(saved_file)
HPI_data.plot(legend=None)


#using pickle for pandas
HPI_data.to_pickle('fifty_states_pandas.pickle')
HPI_data2=pd.read_pickle('fifty_states_pandas.pickle')
HPI_data2.head()