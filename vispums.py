#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vispums.py

Use Matplotlib to visually represent data in a 2x2 subplot
"""

# =========================== head block information ==========================
print('----------------------------------------------------------------------')
print('Data-51100, Summer Session 1 Year 2022')
print('NAME: Lava Veeramachaneni, Sairam Ponguluri, and Victoria Griffin')
print('Programming Assignment #6\n')

# ========================== import correct libraries =========================
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore") #used for a bug found in Matplotlib 3.0
    


# ================+ read csv file and create initial figure ===================

# Import csv file
raw = 'ss13hil.csv'

# Create dataframe with just the needed columns from csv file
df = pd.read_csv(raw, usecols=['WGTP', 'MRGP', 'VEH', 'HHL', 'HINCP', 'TAXP', 'VALP'], skipinitialspace = True)

# Create figure for placing subplots
fig = plt.figure(figsize = [15,10], facecolor = 'white')

# Figure title 
fig.suptitle('Group 3 Output', y = 1.02, fontweight = 'bold', fontsize = 'xx-large')



# ================ pie chart for number of household languages ================
ax1 = fig.add_subplot(2, 2, 1) #create a subplot in upper left corner

# Create pie chart
hhl = df['HHL'].value_counts()
ax1.pie(hhl, startangle=240, pctdistance = 1.0)
ax1.axis('equal')

#Set title, label, and legend
ax1.set_title('Household Languages')
ax1.set_ylabel('HHL', size = 'medium')
ax1.legend(labels = ['English Only', 'Spanish', 'Other Indo-European', 'Asian and Pacific Island Languages', 'Other'],\
           loc = 'upper left')

    

# ====================== histogram on household income ========================
ax2 = fig.add_subplot(2, 2, 2) #create a subplot in the upper right corner
hincp = df['HINCP']

#KDE plot superimposed over histogram
hincp.plot(kind = 'kde', color = 'black', ls = 'dashed')

#Replace all NaN and negative values in HINCP column with 1
df.loc[df.HINCP < 1, 'HINCP'] = 1
hincp = hincp.fillna(1)
logbin = np.logspace(1, 7, num = 100)

# Histogram plot
ax2.hist(hincp, bins = logbin, facecolor = 'g', alpha = 0.5, histtype = 'bar', \
         density = True, range = (0, len(df['HINCP'])))

#Set title and labels
ax2.set_xscale('log')
ax2.set_title('Distribution of Household Income')
ax2.set_xlabel('Household Income($)- Log Scaled', size = 'medium')
ax2.set_ylabel('Density', size = 'medium')

#Set y axis values
h_vals = np.arange(0, 0.000025, step = 0.000005)
ax2.set_yticklabels(['{:.6f}'.format(x) for x in h_vals],fontsize = 'medium')
ax2.grid(color = 'grey', linestyle = '-', linewidth = 1, alpha = 0.2)



# ============ bar chart on thousands of households for each VEH ==============
ax3 = fig.add_subplot(2, 2, 3) #create a subplot in lower left corner

# Create a bar chart
veh_data = (df.groupby('VEH')['WGTP'].sum())/1000

ax3.bar(veh_data.index, veh_data.values, color = 'r', alpha = 0.8, width = 0.9 )

#Set titles and axis labels
ax3.set_title('Vehicles Available in Households')
ax3.set_xlabel('# of Vehicles', size = 'medium')
ax3.set_ylabel('Thousands of Households', size = 'medium')



# ===================== scatterplot on TAXP vs. VALP ==========================
ax4 = fig.add_subplot(2, 2, 4) #create subplot in lower right corner

#Create series from df dataframe
valp_series = Series(df['VALP'])
taxp_series = Series(df['TAXP']).replace({1:0,2:1,3:50,4:100,5:150,6:200,7:250,8:300,9:350,10:400,11:450,12:500,13:550,14:600,15:650,16:700,17:750,18:800,19:850,20:900,
                                                    21:950,22:1000,23:1100,24:1200,25:1300,26:1400,27:1500,28:1600,29:1700,30:1800,31:1900,32:2000,33:2100,34:2200,35:2300,36:2400,
                                                    37:2500,38:2600,39:2700,40:2800,41:2900,42:3000,43:3100,44:3200,45:3300,46:3400,47:3500,48:3600,49:3700,50:3800,51:3900,52:4000,
                                                    53:4100,54:4200,55:4300,56:4400,57:4500,58:4600,59:4700,60:4800,61:4900,62:5000,63:5500,64:6000,65:7000,66:8000,67:9000,68:10000})
#Create scatterplot
plt.scatter(valp_series,taxp_series,marker='o',s = df['WGTP']/5,c=df['MRGP'],cmap='seismic',vmax=5000, alpha=.20)

#Set x axis ticks and tick labels
x_val_ax4 = np.arange(0, 1200000, step = 200000)
ax4.ticklabel_format(useOffset=False, style='plain')
ax4.set_xlim(0, 1200000)

#Set y-axis ticks and tick labels
ax4.set_ylim(0, 10800)
ax4.set_yticklabels(labels = ['0', '2000', '4000', '6000', '8000', '10000'],fontsize = 'medium')

#Set titles and axis labels
ax4.set_title('Property Taxes vs Property Values')
ax4.set_xlabel('Property Value ($)', size = 'medium')
ax4.set_ylabel('Taxes ($)', size = 'medium')

#Set colorbar with 37 white minor ticks
cbar = plt.colorbar(ticks=[1000,2000,3000,4000, 5000])
cbar.ax.set_ylabel('First Mortgage Payment (Monthly $)', size = 'medium', rotation=90)
cbar.ax.hlines(y=[4868.42, 4736.84, 4605.26, 4473.68, 4342.1, 4210.52, 4078.94,\
                  3947.36, 3815.78, 3684.2, 3552.62, 3421.04, 3289.46, 3157.88, 3026.3,\
                  2894.72, 2763.14, 2631.56, 2499.98, 2368.4, 2236.82, 2105.24,\
                  1973.66, 1842.08, 1710.5, 1578.92, 1447.34, 1315.76, 1184.18, 1052.6,\
                  921.02, 789.44, 657.86, 526.28, 394.7, 263.12, 131.58], xmin= 0, xmax= 1000000, color= 'w')



# =========================== adjust subplots =================================
plt.subplots_adjust(left=0.1,
                    bottom = 0.1,
                    right = 0.9,
                    top = 0.9,
                    wspace = 0.4,
                    hspace = 0.5)



# ========================= save file as pums.png =============================
plt.tight_layout()
plt.savefig('pums.png', dpi = 400, bbox_inches = 'tight')
