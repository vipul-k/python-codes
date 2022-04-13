# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 21:22:04 2021

@author: Vipul Kumar
"""
def vectorize(func):   
    '''
    Takes a single argument function, defines a new function which can take
    any number of positional argumnets and feeds them one by one to into 
    single argument function.
    

    Parameters
    ----------
    func : Function
        Single argument function.

    Returns
    -------
    new_func: Function
        Takes any number of positional arguments and feeds them to "func" one 
        by one.

    '''
    def _new_func(*args):
        '''
        Takes any number of positional arguments and feeds them to "func" one 
        by one.

        Parameters
        ----------
        *args : undefined
            Values to be fed to original one argument function

        Returns
        -------
        ret_list : List
            Values obtained on each invocation of origina one argument function.

        '''
        ret_list = []
        for i in args:

            ret_list.append(func(i))

        return ret_list
            
    return _new_func

if __name__ == '__main__':

    new_func_check = vectorize(str.upper)
    print(new_func_check("a","A","c"))
    





        