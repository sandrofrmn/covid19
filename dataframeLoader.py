# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:56:49 2021

@author: imsan
"""

import pandas as pd

def loadData():
    df = pd.read_excel("C:/Users/imsan/Desktop/School/Minors/Data Science/Casus/CASUS COVID-19/data_countries_all_with_relatives.xlsx", sheet_name=None)
   
    return df