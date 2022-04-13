# -*- coding: utf-8 -*-
"""
@author: Vipul Kumar

"""
import numpy as np
import matplotlib.pyplot as plt


class TimeSeries():
    def __init__(self, path: str, col_num: int) -> None:
        '''
        TimeSeries class encapsulates the file parsing, computation,
        and plotting for the time seies data.

        Parameters
        ----------
        path : str
            Path of the csv file
        col_num : int
            Column containing the target data.

        Returns
        -------
        None.

        '''
        raw_data = np.genfromtxt(path, delimiter=',', skip_header=1)
        self.length = len(raw_data)
        self.data = np.vstack([np.linspace(0, self.length-1, self.length),
                               raw_data[:, col_num-1]]).T

    def plot_data(self) -> None:
        '''
        Plots the time series data.

        Returns
        -------
        None.

        '''

        fig, ax = plt.subplots()
        self.data[:, 0] = np.arange(48)
        ax.plot(self.data[:, 0], self.data[:, 1])

        ax.set( title="Libraries Wifi", 
            xlabel="Month", ylabel="Number of Sessions");

    def moving_average(self, m: int) -> np.ndarray:
        '''
        Calculates the moving average of the time seriess data

        Parameters
        ----------
        m : int
            Order/window of moving average

        Returns
        -------
        data_mov_avg : np.ndarray
            Numpy array contating the moving average values.

        '''
        data_mov_avg = np.convolve(self.data[:, 1], np.ones(m), 'valid') / m

        fig, ax = plt.subplots()

        k = int((m-1)/2)
        ax.plot(self.data[k:-k, 0], self.data[k:-k, 1],
                color = 'blue', label = "Actual")
        ax.plot(self.data[k:-k, 0], data_mov_avg, color = 'red',
                linestyle = "dotted", label = "Moving Average")
        ax.legend()
        ax.set(title="Libraries Wifi", 
           xlabel="Month", ylabel="Number of Sessions");        
        return data_mov_avg

    def linear_reg_y0(self, y : np.ndarray, m : int) -> np.ndarray:
        '''
        Linear regression model on the tme series data with
        intercept fixed at 0.

        Parameters
        ----------
        y : np.ndarray
            Numpy array contating the moving average values.
        m : Order/window of the moving average
            DESCRIPTION.

        Returns
        -------
        beta : Array
            Contains m coefficients in y = mx linear equation
        R : Array
            Residual obtained by current model

        '''
        k = int((m-1)/2)
        beta, R, _, _ = np.linalg.lstsq(self.data[k:-k,0,np.newaxis],
                                            y, rcond = None)
        fig, ax = plt.subplots()
        ax.plot(self.data[k:-k,0], y, 'o', label='Original data',
                markersize=10)
        ax.plot(self.data[k:-k,0], beta*self.data[k:-k,0],
                'r', label='Fitted line : Y-Int = 0')
        ax.legend()
        ax.set(title="Linear Model : Y Intercept fixed at Zero", 
           xlabel="Month", ylabel="Number of Sessions"); 
        return beta, R
    
    def linear_reg_yInt(self, y : np.ndarray, m : int) -> np.ndarray:
        '''
        Linear regression model on the toime series data.

        Parameters
        ----------
        y : np.ndarray
            Numpy array contating the moving average values.
        m : Order/window of the moving average
            DESCRIPTION.

        Returns
        -------
        beta : Array
            Contains c, m coefficients in y = mx + c linear equation
        R : Array
            Residual obtained by current model

        '''
        k = int((m-1)/2)
        A = np.full((self.length-(2*k),2),1)
        A[:,1] = self.data[k:-k,0]
        beta, R, _, _ = np.linalg.lstsq(A, y, rcond = None)
        fig, ax = plt.subplots()
        ax.plot(self.data[k:-k,0], y, 'o', label='Original data',
                markersize=10)
        ax.plot(self.data[k:-k,0], beta[0] + beta[1]*self.data[k:-k,0],
                'r', label='Fitted line')
        ax.legend()
        ax.set(title="Linear Model", 
           xlabel="Month", ylabel="Number of Sessions"); 
        return beta, R
    
if __name__ == "__main__":    
    timeseries = TimeSeries("E:\Courses\Python\project 2\Libraries Wifi.csv", 
                            3)
    timeseries.plot_data()
    
    data_mov_avg = timeseries.moving_average(7)
    beta_y0, R_y0 = timeseries.linear_reg_y0(data_mov_avg, 7)
    beta, R = timeseries.linear_reg_yInt(data_mov_avg, 7)
    
    if R_y0 < R:
        print("First mode is better")
    elif R == R_y0 :
        print("Both models perform the same")
    else:
        print("Second model is better")
        
        