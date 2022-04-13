# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:35:09 2021

@author: Vipul Kumar
"""
def isect(s1, s2):
    """
    Purpose : Finds the unique integers that appear in both lists and contain the digit 2. There should be no duplicates
    in the results.
    Parameters : Takes two str, each representing a comma-separated sequence of integers.
    Return value : Return the result as a sorted list of int.
    """
    # convert the string into list of integers
    l1 = [int(i) for i in s1.split(",")]
    l2 = [int(i) for i in s2.split(",")]
    #get the intersection of the two lists
    l3 = [value for value in l1 if value in l2]
    #remove duplicates
    l3 = list(set(l3))
    #sort
    l3.sort()
    
    #check wether digit 2 is contaied in the integer
    for i in l3:
        if "2" not in str(i):
            l3.remove(i)
    return l3
            
    
if __name__ == '__main__':
    print(" Provide two str, each representing a comma-separated sequence of integers.")
    s1 = input().strip()
    s2 = input().strip()
    
    print(isect(s1,s2))
    

    
    