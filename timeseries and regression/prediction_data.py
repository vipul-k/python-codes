# -*- coding: utf-8 -*-
"""
@author: Vipul Kumar

"""
import numpy as np
import matplotlib.pyplot as plt

class PredictionData():
    
    def __init__(self, path : str, target : str) -> None:
        '''
        PredictionData class encapsulates the file parsing, computation, 
        and plotting

        Parameters
        ----------
        path : str
            Pat o the csv file containg the prediction data.
        target : str
            Name of the target variable

        Returns
        -------
        None.

        '''
        with open(path) as f:
            self.header = f.readline().strip().split(",")
            self.data = np.genfromtxt(f, delimiter = ',')
            
        self.target = target
        self.target_col = self.header.index(target)
        
    def scatter_plot(self) -> None:
        '''
        Generates scatter plot for all the features vs target variable.

        Returns
        -------
        None.

        '''
        for index, element in enumerate(self.header):
            if element != self.target:
                fig, ax = plt.subplots()
                ax.scatter(self.data[:,index], self.data[:,self.target_col],
                           marker="+", c="green", s=30);
                ax.set(title = f"{element} vs {self.target}",
                       xlabel=element, ylabel=self.target);
    def normalize(self) -> np.ndarray:
        '''
        Standardize the data so that it has a mean of zero and a 
        standard deviation of one

        Returns
        -------
        data_norm : np.ndarray
            Standardized data

        '''
        data_norm = self.data.copy()
        data_norm -= np.mean(data_norm, axis=0)
        data_norm /= np.std(data_norm, axis=0)
        return data_norm
    
    def linear_reg(self, data_norm : np.ndarray) -> list:
        '''
        Train linear regression models corresponding to each eature 
        in the dataset

        Parameters
        ----------
        data_norm : np.ndarray
            Standardized data

        Returns
        -------
        header    :List
            List of features
        residuals : List
            List o residuals corresponding to each feature
        coeff : List
            List of coefficients corresponding to each feature

        '''
        residuals = []
        coeff = []
        for index, element in enumerate(self.header):
            if element != self.target:
                A = np.vstack([np.ones(len(data_norm)), data_norm[:,index]]).T
                beta, R, _, _ = np.linalg.lstsq(A, 
                                data_norm[:, self.target_col], rcond = None)
                fig, ax = plt.subplots()
                ax.scatter(data_norm[:,index], data_norm[:,self.target_col],
                           marker="+", c="green", s=30);
                ax.plot(data_norm[:,index], beta[0] + 
                        beta[1]*data_norm[:,index],
                        'r', label='Fitted line')
                ax.legend()
                ax.set(title = f"Linear Model: {element} vs {self.target}",
                       xlabel=element, ylabel=self.target);
                residuals.append(R[0])
                coeff.append(beta)
        best_pred = self.header[residuals.index(min(residuals))]
        print("Best predictor of", self.target, "is", best_pred )
        return self.header, residuals, coeff
        
if __name__ == "__main__":
    pred = PredictionData(
        "E:\Courses\Python\project 2\California house prices.csv", 
        "House_price")
    pred.scatter_plot()
    data_norm = pred.normalize()
    feature, R, beta = pred.linear_reg(data_norm)