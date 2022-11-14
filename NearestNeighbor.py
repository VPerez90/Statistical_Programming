#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nearest Neighbor Classification Program

Utilizes NumPy Python Library and Machine Learning Concepts/Fundamentals to:
Wrtie a program that learns and in the end, classifies (with sufficient accuracy) 
three types of iris plants based on their sepal and petal length and width.

"""

# Head Block Information
print('----------------------------------------------------------------------')
print('Data-51100, Summer Session 1 Year 2022')
print('NAME: Victoria Griffin')
print('Programming Assignment #3')

import numpy as np

# Load training and testing files from computer 
train_file = 'iris-training-data.csv'
test_file = 'iris-testing-data.csv'


# Create a 1D and 2D array for training file:
# 2D array for sl, sw, pl, pw: columns 0, 1, 2, 3 respectively
# 1D array for flower label: column 4 from file
training_attributes = np.loadtxt(train_file, delimiter=',', usecols=(0,1,2,3))
training_labels = np.loadtxt(train_file, dtype='<U15', delimiter=',', usecols=(4))


# Create a 1D and 2D array for testing file
# 2D array for sl, sw, pl, pw: columns 0, 1, 2, 3 respectively
# 1D array for flower label: column 4 from file
testing_attributes = np.loadtxt(test_file, delimiter=',', usecols=(0,1,2,3))
testing_labels = np.loadtxt(train_file, dtype='<U15', delimiter=',', usecols=(4))

# Testing labels put into array of shape 75 x 1
testing = np.array((testing_labels)).reshape(75,1)


# Mathematical equation for finding the distances (saved in an array of 75 x 75)
distances = np.sqrt(np.square(testing_attributes[:,np.newaxis]-training_attributes).sum(axis=2))


# Indexes where each minimum is found
all_mins = np.argmin(distances, axis=1)
count = np.count_nonzero(all_mins) # will use for calculating accuracy later


# Array of predicted iris types based on testing data vs. training data put 
# into array of shape 75 x 1
predicted_iris = testing_labels[all_mins]
predicted = np.array((predicted_iris)).reshape(75,1)


# Range of numbers 1-75 put into an array of shape 75 x 1
numbers = np.arange(75)
numbers_plus_one = numbers+1
num = np.array((numbers_plus_one)).reshape(75,1)


'''
Code for concatenating 3 arrays and formatting the concatenated array to
include the following:
    -No brackets
    -No string quotations
    -Commas between 0-1 and 1-2 columns with no spaces
    -All printed to leftmost part of console
''' 
print()
print('#, True, Predicted')

# For concatenating 3 arrays
concat_array = np.concatenate((num, testing, predicted), axis=1)

# For formatting to project specifications --> listed above
array_to_list = np.array(concat_array.tolist())
no_string_array = (np.array2string(array_to_list, separator=','\
                                   , formatter={'str_kind': lambda x: x}))
final_array = str(no_string_array).replace('[','').replace('[','')\
    .replace(' ', '').replace(']','  ').replace('  ,', '')

print(final_array) #final array printed


# Code for calculating the percent accuracy
number_same = np.count_nonzero(testing_labels == predicted_iris) # find how many are the same
percent_accuracy = (number_same/count)*100 #formula for % accuaracy
decimal_format = '{:.2f}'.format(percent_accuracy) #fomratted to 2 decimals


# Print accuracy to console
print('Accuracy: '+ str(decimal_format) + '%')
print('----------------------------------------------------------------------')



