# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:32:10 2021

@author: Vipul Kumar
"""

import statistics

def mean_stddev_stdlib(dice):
    '''   

    Function calculates the mean and standard deviation of dice values of each character using inbuilt library functions    

    Parameters
    ----------
    dice : Dictionary
        Contains dice values for each character

    Returns
    -------
    dice_stat : Dictionary
       Contains the mean and standard deviatioj of dice values of each character
       
    

    '''
    dice_stat = dict()
    for key in dice:
        dice_stat[key] = [statistics.mean(dice[key]),statistics.pstdev(dice[key])]
    return dice_stat

def mean_value(l):
    '''
    User defined function to calculate mean of a list of numbers

    Parameters
    ----------
    l : list of numbers
        Contains dice values for each character

    Returns
    -------
    mean of l
       
       
    '''   
    return sum(list(l))/len(list(l))
 
def stddev(l):
    '''
    User defined function to calculate standard deviation of a list of numbers

    Parameters
    ----------
    l : list of numbers
        Contains dice values for each character

    Returns
    -------
    standard deviation of l
       
       
    '''   
    mean = mean_value(l)
    variance = sum([((x - mean) ** 2) for x in l]) / len(l)
    return variance**0.5

def mean_stddev_no_stdlib(dice):
    '''
    Function calculates the mean and standard deviation of dice values of each character using user defined functions

    Parameters
    ----------
    dice : Dictionary
        Contains dice values for each character

    Returns
    -------
    dice_stat : Dictionary
       Contains the mean and standard deviation of dice values of each character
       
    '''
    dice_stat = dict()
    for key in dice:
        dice_stat[key] = [mean_value(dice[key]),stddev(dice[key])]
    return dice_stat

def mean_stddev_sorted(dice):
    '''
    Function sorts the dictionary containing mean and standard deviation

    Parameters
    ----------
    dice : Dictionary
        Contains dice values for each character

    Returns
    -------
    l : list
       Returns asortedsequence such that each element is a nested sequence of two items:  character nameand another nested sequence of 2 items.  The items of the innermost nested sequence are mean andstandard deviation
    '''
    dice_stat = mean_stddev_stdlib(dice)
    l = []
    for key in dice_stat:
        l.append([key, dice_stat[key]])

    l.sort(key = lambda x : [x[1][0],x[1][1]])
    return l

def mean_stddev_filtered(dice):
    '''
    Function sorts the dictionary containing mean and standard deviation and filters for mean >= 3.5

    Parameters
    ----------
    dice : Dictionary
        Contains dice values for each character

    Returns
    -------
    sort_filt : list
      Returns a nested sequence formatted and sorte filtered for mean >= 3.5 
    '''
    dice_sort = mean_stddev_sorted(dice)
    sort_filt = [x for x in dice_sort if x[1][0] >= 3.5]      
    return sort_filt

if __name__ == '__main__':
    dice = {'Boo' : (0, 0, 5, 5, 7, 7),'Bowser' : (0, 0, 1, 8, 9, 10),'BowserJr' : (1, 1, 1, 4, 4, 9),'Daisy' : (3, 3, 3, 3, 4, 4),'DiddyKong' : (0, 0, 0, 7, 7, 7),'DonkeyKong' : (0, 0, 0, 0, 10, 10),'DryBones' : (1, 1, 1, 6, 6, 6),'Goomba' : (0, 0, 3, 4, 5, 6),'HammerBro' : (0, 1, 1, 5, 5, 5),'Koopa' : (1, 1, 2, 3, 3, 10),'Luigi' : (1, 1, 1, 5, 6, 7),'Mario' : (1, 3, 3, 3, 5, 6),'MontyMole' : (0, 2, 3, 4, 5, 6),'Peach' : (0, 2, 4, 4, 4, 6),'PomPom' : (0, 3, 3, 3, 3, 8),'Rosalina' : (0, 0, 2, 3, 4, 8),'ShyGuy' : (0, 4, 4, 4, 4, 4),'Standard' : (1, 2, 3, 4, 5, 6),'Waluigi' : (0, 1, 3, 5, 5, 7),'Wario' : (6, 6, 6, 6, 0, 0),'Yoshi' : (0, 1, 3, 3, 5, 7)}
    dice_stat1 = mean_stddev_stdlib(dice) 
    #print(dice_stat1)       
    dice_stat2 = mean_stddev_no_stdlib(dice) 
    #print(dice_stat2) 
    dice_sort = mean_stddev_sorted(dice) 
    #print(dice_sort) 
    dice_sort_filt = mean_stddev_filtered(dice) 
    print(dice_sort_filt)
        