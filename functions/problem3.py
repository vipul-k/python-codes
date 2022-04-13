# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:02:30 2021

@author: Vipul Kumar
"""
def newton(f, f_pr, x_0, tol, max_iter):
    '''
    This function implements the Newton-Raphson method

    Parameters
    ----------
    f : function
        f is a function that implements f(x). Assume that f takes a single numerical argument and returns a
single numerical value.
    f_pr : unction
        f_pr is a function that implements f0(x). Assume that f_pr takes a single numerical argument and
returns a single numerical value.
    x_0 : float
        x_0 is an initial guess at a root.
    tol : float
        tol is the absolute tolerance used to end the recurrence. That is, when jxn+1 􀀀 xnj < tol, then xn+1
should be returned as the result.
    max_iter : integer
        max_iter is the maximum number of recurrences. That is, when n  max iter, then xn+1 should be
returned as the result, even if jxn+1 􀀀 xnj  tol

    Returns
    -------
    The return value is xn+1, which results from either tol or max iter being reached, as described above.

    '''
    #assign initial value to x_n using the passed parameter
    x_n = x_0
    #for loop for maximum possible iterations = max_iter
    for i in range(0,max_iter):
        #evaluate x_n1 using the formula for Newton-Raphson method
        x_n1 = x_n - (f(x_n)/f_pr(x_n))
        #check if change in value of x_n is below tolerance limit and return x_n1 if true
        if abs(x_n1 - x_n) < tol:
            return x_n1
        #assign value of x_n1 to x_n for next iteration
        x_n = x_n1
        
    return x_n1


def f(x):
    # example function used to test the code
    return (x - 1) ** 2

def f_pr(x):
    #example function used to test the code
    return 2*(x-1)

if __name__ == '__main__':
   
    print(newton(f, f_pr, 0, 1e-16, 1))
        
        
            