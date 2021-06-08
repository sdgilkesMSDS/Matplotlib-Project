#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MSDS 670 Matplotlib Project
By Savannah Gilkes
"""

#%%
import os

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv (r'/Users/savannahgilkes/Downloads/Denver Crime 2001-2013.csv')
print(df)

#Creating barplot depiting the average rate of different crimes over a twelve year period (2001-2013) in Denver

data = {'Murders': 47,
        'Rapes': 341,
        'Robberies': 1179,
        'Assaults': 2541, 
        'Burglaries': 5779, 
        'Thefts': 14155,
        'Auto Thefts': 5353,
        'Arson': 181}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

fig, ax = plt.subplots()
ax.barh(group_names, group_data)

ax.set_title('Average Crime Rates in Denver 2001 to 2013')
ax.set_xlabel('Total Incidents')

fig.savefig('AverageCrime.png', transparent=False,bbox_inches="tight")

#%%

#Creating scatter plot showing auto thefts in Denver from 2001 to 2013

data2 = {'2001': 6835,
        '2002': 7441,
        '2003': 7128,
        '2004': 7538,
        '2005': 8025,
        '2006': 6374,
        '2007': 5121,
        '2008': 3596,
        '2009': 3844,
        '2010': 3226,
        '2011': 3587,
        '2012': 3670,
        '2013': 3487}

group_data2 = list(data2.values())
group_names2 = list(data2.keys())
group_mean2 = np.mean(group_data2)

fig, ax = plt.subplots(figsize=(9,6))
ax.scatter(group_names2, group_data2)
ax.plot(group_names2, group_data2)

ax.set_title('Denver Auto Thefts', fontsize = 15)
ax.set_xlabel('Year')
ax.set_ylabel('Total Thefts')

fig.savefig('AutoThefts.png', transparent=False,bbox_inches="tight")

#%%

#Creating scatter plot showing thefts in Denver from 2001 to 2013

data3 = {'2001': 14621,
        '2002': 15467,
        '2003': 14839,
        '2004': 15590,
        '2005': 18518,
        '2006': 13376,
        '2007': 11594,
        '2008': 10547,
        '2009': 12628,
        '2010': 12994,
        '2011': 14040,
        '2012': 14544,
        '2013': 15306}

group_data3 = list(data3.values())
group_names3 = list(data3.keys())
group_mean3 = np.mean(group_data3)

fig, ax = plt.subplots(figsize=(9,6))
ax.scatter(group_names3, group_data3)
ax.plot(group_names3, group_data3)

ax.set_title('Denver Thefts', fontsize = 15)
ax.set_xlabel('Year')
ax.set_ylabel('Total Thefts')

fig.savefig('Thefts.png', transparent=False,bbox_inches="tight")








