# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:25:35 2021

@author: hp
"""
def prime_generator():
    '''
    Generator function that yields successive prime numbers starting at 2

    Yields
    ------
    curr : Int
        Prime number

    '''
    #current number
    curr = 2
    #list used to cache already discovered prime numbers
    primes = []
    while(True):        
        if len(primes) > 0:
            ind = 0
            for num in primes:
                if curr%num == 0:
                    ind+=1
                    break
            if ind == 0:
                primes.append(curr)
                yield curr
        else:
            primes.append(curr)
            yield curr
        curr+=1
        
if __name__ == '__main__':
    gen = prime_generator()
    for i in range(10):
        print(next(gen))
                
                
                        
                    
            
    