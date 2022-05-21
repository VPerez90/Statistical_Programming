#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program uses the concept of k-means clustering for a 1D list of points. 
The program, without the use of Python libraries, separates the points into
k number of clusters (with the closest points grouped together),
and updates until clusters no longer change.
"""

# Head Block Information
print('----------------------------------------------------------------------')
print('Data 51100 - Summer Session 1 Year 2022')
print('Victoria Griffin, Lava Veeramachaneni, and Ashay Bajpai ')
print('Programming Assignment #2')

'''
Starts program with file input of data points and asking user for the
number of clusters
'''

#input data from file and save it to a list
input_file = 'prog2-input-data.txt'
f = open(input_file)
data = [float(line.rstrip()) for line in f]
print()

#Asks user for the number of clusters
k = int(input('Enter the number of clusters: '))

#Will catch accidental mistakes by user -- not for continuous mistakes
if k == 0:
    print('Please enter a number greater than 0')
    k = int(input('Enter the number of clusters: '))
if k < 0:
    print('Please enter a positive number')
    k = int(input('Enter the number of clusters: '))
if k > len(data):
    print('Number is too large, please choose a number smaller than the number of data points')
    k = int(input('Enter the number of clusters: '))

'''
This section creates the following dictionaries:
    centroids --> for saving number of k number of clusters to the first k number of points
    clusters --> for saving the points to the closest cluster
    point_assigments --> for saving cluster location for each point
    old_point_assignemnts --> for updating clusters until clusters no longer change
'''
#create dictionary for saving first k number of clusters to the first k number of points in the data list
centroids = dict(zip(range(k), data[0:k]))

# creates an dictionary where the keys are 0-(k-1) and the values are empty lists ready for storing points.
clusters = dict(zip(range(k),[[] for i in range(k)]))

#point assignment and old point assignment dictionaries
point_assignments = dict(zip([i for i in data], [0 for i in data]))
old_point_assignments = {}


'''
Next section are all of the functions written for the program:
    dist --> for finding the the distance between two points on a 1D line
    assign_to_clusters --> assigns data points to nearest cluster
    update_location --> calculate new mean of each cluster
'''
# create a funtion for finding the distance between two points on a 1D line
def dist(x, y):
    return abs(x - y)

# create a function that will take a data point and assign it to the nearest cluster
def assign_to_clusters(data, centroids, clusters, point_assignments):
    for i, num in enumerate(data):
        closest_dist = float('inf')
        for j, values in enumerate(centroids):
            if closest_dist > dist(data[i], centroids[j]):
                closest_dist = dist(data[i], centroids[j])
                closest_index = j 
                
        point_assignments[data[i]]= closest_index
        
        clusters[closest_index].append(data[i])
           
# create a function that will calculate the new mean of each cluster
def update_location (clusters, centroids):
    for key, values in enumerate(clusters):
        num_of_points = len(clusters[key])
        new_mean = sum(clusters[key])/num_of_points
        centroids[key] = new_mean


'''
This is the main section of the progam:
    Compares old_point_assignments to _point_assignments
    Calls functions
    Prints information to console
    Updates other important information
'''
     
#will repeat the following steps until the old_point_assignments dict equals point_assignments dict       
n = 1    
while old_point_assignments != point_assignments:
    
    old_point_assignments = point_assignments.copy() #copies current to old
    
    assign_to_clusters(data, centroids, clusters, point_assignments) #calls assign_to_clusters function
    
    update_location(clusters, centroids) #calls update_location function

    #will print current clusters and points within that cluster
    print('Iteration ' + str(n))
    for key, value in clusters.items():
        print(str(key) + ' : ' +  str(value))
    print('\n')
    n += 1 #increases n by 1
    
    clusters = dict(zip(range(k),[[] for i in range(k)])) # resets cluster dict to empty

# Once old_point_assignments equals point_assignments, final data points and cluster assignments will be printed
for key, value in point_assignments.items():
    print('Point ' + str(key) + ' in cluster ' + str(value))


'''
This last section will create a new text file for writing and reading our 
data points and what their cluster assignments is
'''

#Create a new test file
fo = open('prog2-output-data.txt', 'w+')        

#write final data points and cluster assignemnts to new data file
for key, value in point_assignments.items():  
    fo.write('Point ' + str(key) + ' in cluster ' + str(value) + '\n')

#Update and close file
fo.close()

print('----------------------------------------------------------------------')