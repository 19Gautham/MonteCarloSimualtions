import numpy as np
import matplotlib.pyplot as plt
import math


class questionTres(object):
    
    def __init__(self):
        self.mean = 0.5

    """
        This function is used to get a uniform random number between 0 and 1
        We leverage the functionality of the numpy random library to generate a random number
    """
    def getUniformRandomNumberBetweenLimits(self):
        return np.random.uniform(0, 1)

    """
        This function is used to find the expectation of a uniform random variable
    """
    def calc_uniform_rv_expectation(self):
        
        iterations = 4000000
        total = 0
        data_array = []
        for i in range(1, iterations + 1):
            total += self.getUniformRandomNumberBetweenLimits()
            if i % 10000 == 0:
                data_array.append((i, total / i))
        
        # Plotting
        plt.plot([data[0] for data in data_array], [data[1] for data in data_array])
        plt.xlabel('Number of iterations')
        plt.ylabel('Average')
        plt.title('Average vs Number of iterations')

        # Label each data point
        for i in range(len(data_array)):
            if i % 40 ==0:
                plt.text(data_array[i][0], data_array[i][1], f'({data_array[i][0]}, {data_array[i][1]:.7f})', fontsize=8, verticalalignment='bottom')
        
        plt.show()

    """
        A generic function to create histograms
    """
    def plot_histogram(self, data_array, n_val):

        plt.hist(data_array, bins=50, density=True)
        plt.xlabel('Normalized Average')
        plt.ylabel('Frequency')
        plt.title('Normalized Average Histogram [N={}]'.format(n_val))
        plt.show()

    """
        This function is used to solve questions regarding the second part of the project
        regarding the central limit theorem
    """
    def calc_clt(self, n_val):
        
        iterations = 40000
        total = 0
        data_array = []
        # generation of "m" data points
        for _ in range(iterations):
            total = 0
            # sum of n random number values - mean 
            for _ in range(1, n_val+1):
                total += (self.getUniformRandomNumberBetweenLimits() - self.mean)
            data_array.append(total / math.sqrt(n_val))

        self.plot_histogram(data_array, n_val)

if __name__ == "__main__":
    tres = questionTres()
    tres.calc_uniform_rv_expectation()
    tres.calc_clt(2)
    tres.calc_clt(10)

