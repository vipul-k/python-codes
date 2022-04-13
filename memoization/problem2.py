# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:26:54 2021

@author: hp
"""
import collections
import typing
import operator

class cache_class(typing.NamedTuple):
    '''
    Cache class used to construct CacheInfo NamedTuple
    
    Attributes:
        – hits: The number of calls to the function where the result 
        was previously calculated and can be returned from the cache.
        – misses: The number of calls to the function where the result 
        was not previously calculated.
        – maxsize: The maximum number of entries that the cache can store.
        – currsize: The number of entries currently stored in the cache.
    '''
    hits : int = 0
    misses : int = 0
    maxsize : int = 0
    currsize : int = 0
    
    def __repr__(self) -> str:
        '''
        Used to return a string with all the attributes in respone 
        to call to an instance of the class.

        Returns
        -------
        str
            String representation of the instance of the class

        '''
        return f'CacheInfo(hits={self.hits}, misses={self.misses}, maxsize={self.maxsize}, currsize={self.currsize})'
    
def lru_cache(func, maxsize=128):
    '''
    Function wrapper

    Parameters
    ----------
    func : Function
        Any function which is to wrapped in lru_cache
    maxsize : Int, optional
        Maximum size of the cached data. The default is 128.

    Returns
    -------
    Inner Function
        Function that is used to call 'func' with arbitrary 
        number of positional arguments.

    '''
    cache = collections.OrderedDict()  
    cache_data = {'hits' :  0, 'misses'  : 0, 'maxsize'  : maxsize, 
                  'currsize' : 0}
    def Cache_Info():
        '''
        Function used to craete an instance of cache_class corresponding
        to current 'inner' and print the information.


        '''
        CacheInfo = cache_class(cache_data['hits'], cache_data['misses'], 
                                cache_data['maxsize'],
                                cache_data['currsize'])
        print(CacheInfo)       
        
    
    def inner(*args):  
        '''
        Calls func with arbitrary positional arguments.
        Maintains an LRU cache called cache in its closure.
        Have a function attribute cache_info() in its closure that 
        returns CacheInfo.
        Parameters
        ----------
        *args : Undefined type
            Arguments to be passed to func

        Returns
        -------
        value : Undefined type
            Output of 'func' function for 'args' argument/s. 

        '''
        
        #cache_info:str
        
        
        if args in cache:
            value = cache[args]
            cache_data['hits'] += 1
        else:
            value = func(*args)
            cache[args] = value
            
            cache_data['misses'] += 1
            if len(cache) > maxsize:
                cache.popitem(last = False)

        cache.move_to_end(args, last = True)
        cache_data['currsize'] = len(cache)
        
        return value
    
    inner.cache_info = Cache_Info
    return inner    

if __name__ == '__main__':
    inputs = [1, 2, 3, 4, 2, 2, 5, 6, 4, 1, 2, 1, 5]
    cached_mul = lru_cache(operator.mul, maxsize=4)
    print([cached_mul(x, 2) for x in inputs])
    cached_mul.cache_info()
    inputs = ["a", "b", "c", "d", "a", "e", "d", "f", "g", "d", "h"]
    cached_upper = lru_cache(str.upper, maxsize=32)
    print([cached_upper(x) for x in inputs])
    cached_upper.cache_info()
            

                
            