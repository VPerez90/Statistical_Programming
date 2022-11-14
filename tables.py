#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tables.py

Work with ACS PUMS dataset to produce several tables which aggregates the data
using groupby, crosstab/pivot_table, and quantile analysis.

"""

# =========================== Head block information ==========================
print('----------------------------------------------------------------------')
print('Data-51100, Summer Session 1 Year 2022')
print('NAME: Victoria Griffin')
print('Programming Assignment #7\n')


# ============ Import correct libraries and set display options ===============
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:6f}'.format)


# ============================= Read csv file =================================
# Import csv file and create dataframe
df = pd.read_csv('ss13hil.csv', usecols=['WGTP', 'HHT', 'ACCESS', 'HHL', 'HINCP'], skipinitialspace = True)


# Drop NaN values from df
df.dropna(inplace=True)


# ================================ Table 1 ====================================

# Print table header
print('*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***')

# HHT description dict
hht = {
    1 : 'Married couple household',
    2 : 'Other family household:Male householder, no wife present',
    3 : 'Other family household:Female householder, no husband present',
    4 : 'Nonfamily household:Male householder:Living alone',
    5 : 'Nonfamily household:Male householder:Not living alone',
    6 : 'Nonfamily household:Female householder:Living alone',
    7 : 'Nonfamily household:Female householder:Not living alone'}

# Rename HHT column to match sample output while applying hht text dict
df['HHT - Household/family type'] = df['HHT'].apply(lambda id : hht[int(id)])

# Create table 1
table_1 = df.groupby('HHT - Household/family type').agg({ 'HINCP':['mean', 'std', 'count', 'min', 'max'] })

# Column labels for table 1
table_1.columns = ['mean', 'std', 'count', 'min', 'max']

# Sort table 1 by mean in descending order
table_1.sort_values(by='mean', ascending=False, inplace=True)

# Change min and max values to integers
table_1['min'] = table_1['min'].astype(int)
table_1['max'] = table_1['max'].astype(int)

# Print table 1
print(table_1)
print()

# ================================ Table 2 ====================================

# Print table header
print('*** Table 2 - HHL vs. ACCESS - Frequency Table ***')
print('                                              sum ')
print('                                             WGTP ')

# HHL description dict
hhl = {
    1 : 'English only',
    2 : 'Spanish',
    3 : 'Other Indo-European languages',
    4 : 'Asian and Pacific Island languages',
    5 : 'Other language'}

# Rename HHL column to match sample output while applying hhl text dict
df['HHL - Household language'] = df['HHL'].apply(lambda id : hhl[int(id)])

# Create table 2
table_2 = pd.crosstab(index=df['HHL - Household language'], values = df['WGTP'], aggfunc='sum', columns=df['ACCESS'], margins=True, normalize='all')

# Convert values to percentages
table_2 = table_2.applymap(lambda x: '{:.2f}%'.format(x*100))

# Rearrange the columns in table 2
table_2 = table_2.rename(columns = {1.0: 'Yes w/ Subsrc.', 2.0: 'Yes, wo/ Subsrc.', 3.0: 'No', 'All': 'All'})

# Reindex rows so they are in same order as output
new_index = ['English only', 'Spanish', 'Other Indo-European languages', 'Asian and Pacific Island languages', 'Other language', 'All']
table_2 = table_2.reindex(new_index)

# Print table 2
print(table_2)
print()



# ================================ Table 3 ====================================

# Print table header
print('*** Table 3 -  Quantile Analysis of HINCP - Household income (past 12 months) ***')

# Creates equal size quantiles using HINCP data - will split into 3 sections
group = pd.qcut(df['HINCP'], 3, labels=['low', 'medium', 'high'])

# Groupby of HINCP with group
grouped = df['HINCP'].groupby(group)

# Groupby of WGTP with group and find the sum       
grouped_2 = df['WGTP'].groupby(group)
sum_1 = grouped_2.sum()


# Create table 3
table_3 = grouped.describe()[['min', 'max', 'mean']]

# Column labels for table 3
table_3.columns = ['min','max','mean']

# Change min and max values to integers
table_3['min'] = table_3['min'].astype(int)
table_3['max'] = table_3['max'].astype(int)

# Add sum_1 datafrome to table_3 and create column name 'household_count'
table_3['household_count'] = sum_1

# Print table 3
print(table_3)
