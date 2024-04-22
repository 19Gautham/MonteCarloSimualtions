import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import erfc
from scipy.special import erfcinv
from math import pow, log10

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
from scipy.stats import norm


class questionQuatro(object):
    
    def __init__(self):
        self.no_of_samples = int(pow(10, 6))
    
    """
        Generate a matrix of symbols radnomly selected from [-1, 1]
    """
    def generate_symbols(self):
        return np.random.choice([-1, 1], self.no_of_samples)
    
    """
        Generate a matrix of nosie values drawn from a standard Gaussian distribution
    """
    def generate_noise(self):
        return np.random.normal(0, 1, self.no_of_samples)


    # Function to simulate the digital communication system
    def get_experimental_error_probability(self,snr):
        
        snr = pow(10,(snr / 10))
        symbols = self.generate_symbols()
        noise = self.generate_noise()
        received_signals = np.sqrt(snr) * symbols + noise
        
        # An operation on the array to classify if the received signal is to be judged as +1 or -1
        received_symbols = np.where(received_signals > 0, 1, -1)  # Decide received symbols
        
        # Count all values where there is a disagreement between the received and expected values
        error_count = np.sum(received_symbols != symbols)
        
        # Calcualting bit error rate
        ber = error_count / self.no_of_samples
        return ber
    
    """
        Calculating the error probability  using formulas
        based on the CDF of Gaussian random variable
    """
    def get_theoretical_error_probability(self, snrDb):
        snr = 10 ** (snrDb / 10)
        return 0.5 * erfc(np.sqrt(snr / 2))

    """
        Plot the graph the experimental and calcualted values against the SNR
    """    
    def plot_graph(self, snr_range, expt_ber, theoretical_ber):
    
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.semilogy(snr_range, expt_ber, label='Experimental Error Probability / BER')
        plt.semilogy(snr_range, theoretical_ber, label='Calculated Error Probability / BER')
        plt.xlabel('SNR (dB)')
        plt.ylabel('Error Probability')
        plt.title('Error Probability vs. SNR')
        plt.legend()
        plt.grid(True)
        plt.show()

    """
        Main function containg the logic for solving this tasks
    """
    def calc_bit_error_probability(self):

        # check function calcaulate_snr_range to understand calculations for coming with this range
        snr_range = np.linspace(-25, 10, 1000)
        expt_ber = []
        theoretical_ber = []
        
        # Monte Carlo simulations and analytical calculations
        for snr in snr_range:
            expt_val = self.get_experimental_error_probability(snr)
            calc_val = self.get_theoretical_error_probability(snr)
            print("Snr: {}, Expt: {}, Calc: {}".format(snr, expt_val, calc_val))
            
            expt_ber.append(expt_val)
            theoretical_ber.append(calc_val)
        
        self.plot_graph(snr_range, expt_ber, theoretical_ber)

    """
        Calculate the bounds of the snr values to be used while testing
        This function is not used in practice, but were used at arriving at the bounds
    """
    def calculate_snr_range(self):
        # yields 12.59815830348742
        ul = 10 *log10(2 * pow(erfcinv(pow(10, -5)/0.5), 2))
        # the value below is negative infinity
        ll = 10 *log10(2 * pow(erfcinv(1), 2)) 
        
        print("Upper limit: {}".format(ul))
        print("Lower limit: {}".format(ll))       

if __name__ == "__main__":
    quatro = questionQuatro()
    quatro.calc_bit_error_probability()

