# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:45:32 2021

@author: Vipul Kumar
"""
def expand(rng):
    '''  
    This function does following
    An integer range "a-b" is expanded as [a; b), which is left-inclusive/right-non-inclusive.
    There should be no duplicate integers in the returned list.

    Parameters 
    ----------
    rng : String
        Takes a str representing a comma separated list of integers or integer ranges.

    Returns 
    -------
    Return the result as a sorted list of int with the specied integers and expanded integer ranges.

    '''    
    #convert the string into list
    l1 = [i for i in rng.split(",")]
    l2 = []
    #iterate over the list to process the entries
    for i in l1:
        #if entry is a range convert it into individual integers
        if "-" in i:
            a,b = [int(n) for n in i.split("-")]
            for j in range(a,b):
                l2.append(j)
        #else append the integer value
        else:
            l2.append(int(i))
    #remove duplicates and sort the list
    l2 = list(set(l2))
    l2.sort()
    return l2

if __name__ == '__main__':
    print(" Provide the input")
    rng = input().strip()
    
    print(expand(rng))
        