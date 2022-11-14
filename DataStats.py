#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DataStats.py

This program is practicing data cleaning with CPS data using Python 
libraries NumPy and Pandas

"""
# Head Block Information
print('----------------------------------------------------------------------')
print('Data-51100, Summer Session 1 Year 2022')
print('NAME: Victoria Griffin')
print('Programming Assignment #5\n')


#Import Pandas and Numpy, and setting row/column/width for displayed DataFrame
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import numpy as np
import re


def get_start_time(x):
    '''Function to get the starting hour'''
    if str(x[0]) == 'nan':
        return 0
    else:
        return int(re.findall(r'[1-9]', x[0])[0])



def main():
    '''Main function'''
    
    #Reads csv file
    cps_data = pd.read_csv("cps.csv")
    
       
    '''This section finds the highest grade and lowest grades of each school 
    and adds them as new column in cps_data'''
    change_grade = cps_data.loc[list(cps_data.index)[0:661],'Grades_Offered_All'].str.split(',')
   
    cps_data.loc[:, ('Lowest_Grade')] = change_grade.str[0]
    cps_data.loc[:, ('Highest_Grade')] = change_grade.str[-1]
    
    
    '''Creates a new dataFrame pulling just the needed columns from cps_data'''
    selected_cps_data = cps_data[['School_ID', 'Short_Name', 'Is_High_School', \
                                  'Zip', 'Student_Count_Total', 'College_Enrollment_Rate_School',\
                                  'Lowest_Grade', 'Highest_Grade', 'School_Hours']]
    
    
    '''This setion calls the start_time function and returns the number as an
    integer in a new column'''
    start_time = selected_cps_data[['School_Hours']].apply(get_start_time, axis = 1)
    selected_cps_data = selected_cps_data.assign(School_Start_Hour = start_time)
    selected_cps_data.drop(['School_Hours'], inplace = True, axis = 1)
    
    #Finds the distrubution for starting hours
    sum = selected_cps_data.groupby('School_Start_Hour').size()
    
   
    '''This section calulates the mean for College Enrollment for High School, 
    replaces all NaN values with mean in College_Enrollment_Rate_School column, 
    and finds standard deviation for College Enrollment in High Schools new updated 
    column data'''
    college_mean = cps_data['College_Enrollment_Rate_School'].mean() 
    
    #Replaces NaN data with the College_Enrollment_Rate_Mean 
    selected_cps_data['College_Enrollment_Rate_School'] = cps_data['College_Enrollment_Rate_School']\
                                                          .replace(np.nan, college_mean)                                                     
    college_std = cps_data.groupby('Is_High_School')['College_Enrollment_Rate_School'].std()
    
    

    
    
    '''This section calulates the mean and standard deviation for student count
    for non-high school students'''
    non_high_mean = cps_data.groupby('Is_High_School')['Student_Count_Total'].mean()
    non_high_std = cps_data.groupby('Is_High_School')['Student_Count_Total'].std()

   
    
    '''This section calculates the  number of schools outside of loop'''
    zip = selected_cps_data[np.logical_not(selected_cps_data['Zip'].isin([60601, 60602, 60603, 60604, 60605, 60606, 60607, 60616]))]
    zip = zip.shape[0]
    
   
   
    '''Creates a copy of the first 10 rows of selected_cps_data DataFrame''' 
    selected_cps_data_10 = selected_cps_data.head(10)
   
   
    
    '''This section includes all of the formatting and printing to console'''
    #Print table with all required data
    print(selected_cps_data_10)
    print()
    
    #Formats the mean and standard deviation of college enrollment to two decimals
    #and writes output as a sentence
    college_format = '{:.2f}'.format(college_mean)
    std_format = '{:.2f}'.format(college_std[1])
    print('College Enrollment Rate for High Schools = ' + str(college_format) +\
                                                             ' (sd=' + str(std_format + ')'))
    print()
    
    #Formats the mean and standard deviation of non-high school student count to two decimals
    #and writes output as a sentence
    non_high_mean_format = '{:.2f}'.format(non_high_mean[0])
    non_high_std_format = '{:.2f}'.format(non_high_std[0])
    print('Total Student Count for non-High Schools = '+ str(non_high_mean_format) +\
                                                             ' (sd=' + str(non_high_std_format) + ')')
    print()
    
    #Distribution of starting hours
    print('Distribution of Starting Hours')
    print(' 8am: ' + str(sum[8]))
    print(' 7am: ' + str(sum[7]))
    print(' 9am: ' + str(sum[9]))
    print()
    
    #Prints number of schools outside the loop
    print('Number of schools outside Loop: ' + str(zip))
    

main()
print('----------------------------------------------------------------------') # end of program

