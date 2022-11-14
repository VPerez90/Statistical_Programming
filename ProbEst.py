#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program computes the conditional probability of the following car aspirations,
std and turbo, given each of the car makes. The program also computes the 
probability of each car make. All results are printed to the console.
"""

# Head Block Information
print('----------------------------------------------------------------------')
print('Data-51100, Summer Session 1 Year 2022')
print('NAME: Victoria Griffin')
print('Programming Assignment #4\n')

import pandas as pd


def read_and_choose_data():
    '''Created fuction to read and choose proper data'''
    cars = pd.read_csv('cars.csv')
    cars_selected_df = cars[['make', 'aspiration']]
    return cars_selected_df


def calculate_conditional_probabilities(cars_selected_df):
    '''This function calculates conditional probability'''
   
    #Creates a dataframe for easy comparison of make and aspiration 
    tabs = pd.crosstab(cars_selected_df.make, cars_selected_df.aspiration)
    
    #Sorts all cars by how many cars there are for each make
    make_counts = cars_selected_df.make.value_counts().sort_index()
    
    #Calculates the conditional probability for std data 
    make_conditional_std = ((tabs['std']/make_counts) *100).round(decimals=2)
    
    #Calculates the conditional probability for aspiration data 
    make_conditional_turbo = ((tabs['turbo']/make_counts) *100).round(decimals=2)
    
    make_conditional_df = pd.DataFrame({'make_name':cars_selected_df['make'].unique(),
                                            'make_conditional_std': make_conditional_std,
                                            'make_conditional_turbo':make_conditional_turbo})
   
    # Formats dict so all numbers print with 2 decimal places
    make_conditional_df['make_conditional_std'] =  make_conditional_df['make_conditional_std'].apply(lambda x: "{:.2f}".format(x))
    make_conditional_df['make_conditional_turbo'] =  make_conditional_df['make_conditional_turbo'].apply(lambda x: "{:.2f}".format(x))
    
    # Lambda function for quick printing of all requirements asked for in project
    print_make_cond_probabilities = lambda x: print('Prob(aspiration=std|make=' + 
                                                    x.make_name + ') = '+ str(x.make_conditional_std)+'%\n'+
                                                    'Prob(aspiration=turbo|make=' + 
                                                    x.make_name + ') = '+ str(x.make_conditional_turbo)+'%')
    # Applies lambda function to make_conditional_df
    make_conditional_df.apply(print_make_cond_probabilities, axis=1)


def calculate_make_probabilities(cars_selected_df):
    '''This function calculates and prints the make probability'''
    # Get total smaple count in csv file 
    N = cars_selected_df['make'].count()
    
    #Sorts all cars by how many cars there are for each make
    make_counts = cars_selected_df.make.value_counts().sort_index()
    
    #Calculates the  probability for car make data 
    make_probabilities = (make_counts/N *100).round(2)

    # Convert series object to dataframe for ease of printing output
    make_probabilities_df = pd.DataFrame({'make_name': cars_selected_df['make'].unique(),
                                          'make_probability': make_probabilities})
    
    # Formats dict so all numbers print with 2 decimal places
    make_probabilities_df['make_probability'] =  make_probabilities_df['make_probability'].apply(lambda x: "{:.2f}".format(x))
    
    # Lambda function for quick printing of all requirements asked for in project
    print_make_probability = lambda x: print('Prob(make=' + x.make_name + ') = '+ str(x.make_probability) +'%')
   
    # Applies lambda function to make_probabilities_df
    make_probabilities_df.apply(print_make_probability, axis = 1)
    
def main():
    '''Main...calls all functions needed for program'''
    cars_selected_df = read_and_choose_data() #calls function to import cars.csv file
    calculate_conditional_probabilities(cars_selected_df) #calls function to print conditional probabilities
    print()
    calculate_make_probabilities(cars_selected_df) #calls function to print make probabilities

main() #calls main
print('----------------------------------------------------------------------')

cars = pd.read_csv('cars.csv')
cars_selected_df = cars[['make', 'aspiration']]
aspir_data = cars_selected_df.pivot_table(index = 'make', columns = 'aspiration', aggfunc = {'make':len}, fill_value=0)
print(aspir_data)
                             