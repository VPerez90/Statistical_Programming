#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OnlineStats.py
Created on Mon May 9 11:38:00 2022

@author: Victoria
Programming Assignment #1
Data 51100 - Summer Session 1 Year 2022
"""

# Head Block Information
print('----------------------------------------------------------------------')
print('Data 51100 - Summer Session 1 Year 2022')
print('Victoria Griffin')
print('Programming Assignment #1')

#Create empty list for storing user input numbers
list_num = []

# Format printing for original string output
format_string = 'Mean is %.1f variance is 0'

#Get initial user input
num = int(input('Enter a number: '))
if num>=0:
    #Add input from user to empty list
    list_num.append(num)

    #Print information for the first number input
    print(format_string % (num))

    #Variable n ---> used inside while loop
    n = 1

    #Initial sample mean
    mean = num/1

    #Initial sample variance
    sample_var = 0

    #Set up loop for input numbers 2 -----> end
    #Start with a second number input to list_num 
    num = int(input('Enter a number: '))
 
#While loop that cycles until condition is false
while num >=0:
    list_num.append(num)
    
    #Increment n by 1
    n = n + 1
    
    #Online mean formula
    online_mean = mean + ((list_num[n-1]-mean)/n)
    
    #Online variance formula
    online_var = (((n-2)/(n-1))*sample_var) \
        +(((list_num[n-1]-mean)**2)/n)
  
    #Update mean and sample_var variables
    mean = online_mean
    sample_var = online_var
    
    #Convert to string for analysis
    string_ov = str(sample_var)
    
    #If-else statement for printing variance numbers 
    if '.0' in string_ov or '.5' in string_ov:
        online_var = online_var
    else:
        formatted_ov = '{:.11f}'.format(online_var)
        online_var = formatted_ov
        
    #Print updated mean and variance
    print('Mean is ' +str(online_mean) + ' variance is ' + str(online_var))
   
    #Repeat loop while num>=0
    num = int(input('Enter a number: '))

#Indicates end of program
print('----------------------------------------------------------------------')