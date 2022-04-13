# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:47:31 2021

@author: Vipul Kumar
"""
def fill_completions(filename): 
    '''
    Funtion is used to create a completion dictionary of words

    Parameters
    ----------
    filename : String
        Filepath + Name

    Returns
    -------
    c_dict : Dictionary
    keys = every possible combination of index and character occuring in the words obtained from text file
    values = all the words corresponding to the combination of index and character

    '''

    text_file = open(filename, 'r')
    text = text_file.read()

#cleaning
    text = text.lower()
    words = text.split()
    words = [word for word in words if word.isalpha()]
    
    #completion dictionary
    c_dict = dict()
    
    for word in words:
        for c in word:
            if (word.index(c), c) in c_dict:
                c_dict[word.index(c), c].append(word)
            else:
                c_dict[word.index(c), c] = [word]
    for key in c_dict:
        c_dict[key] = set(c_dict[key])
    return c_dict

def find_completions(prefix, c_dict):
    '''
    Function is used to give 

    Parameters
    ----------
    prefix : String
        Word to be completed
    c_dict : Dictionary
        Completion Dictionary

    Returns
    -------
    TYPE
        Set of all possible completion of the preix provided

    '''
    l = []
    for i in range(0,len(prefix)):
        print(i, prefix[i])
        if(i, prefix[i]) in c_dict:
            if len(l) == 0:
                l = c_dict[i, prefix[i]]
            else:
                l_set = set(l)
                l = list(l_set.intersection(c_dict[i, prefix[i]]))
                         
        else:
            return set([])
        
        if len(l) == 0:
            return set([])
        i+=1
    return set(l)
        
def main():
    '''
    This function is defined to test the program

    –Calls fill_completionsto create a completions dictionary from articles.txt.  This file containsthe text of recent articles pulled from BBC.
    –Repeatedly prompts the user for a prefix to complete.
    –For each prefix, callfind_completionsto get the set of possible completions.
    –Print thesortedset of completions, with one word per line.  If no completions are possible, print“No completions”.
    –If the user enters “quit”, end the program.
    –Note that thismainfunction is not used in the automated unit tests, so exact formatting of theoutput is not a concern.

    '''
    #print(" provide a filepath + fileanme")
    #filename = input()
    #c_dict = fill_completions(filename)
    c_dict = fill_completions('E:/Courses/Python/articles3.txt')
    while (True):
        print("\nProvide a prefix")
        prefix = input().strip().lower()
        if prefix == "quit":
            break
        else:
            l_set = find_completions(prefix, c_dict)
        if len(l_set) == 0:
            print("No completions")
        else:
            for word in list(l_set):
                print(word)        
        
        
if __name__ == '__main__':
    main()
