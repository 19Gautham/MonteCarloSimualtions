import numpy as np
import math

class questionUno(object):
    
    def __init__(self):
        # To check the points at which the difference
        # between the calculated PiN and Pi is less than
        # the given boundaries
        self.boundaries = [1, 0.1, 0.01, 0.001]

    """
        This function is essentially used to check if the distance to the given
        co-ordinate fromt he origin is less than or equal to 1
    """
    def isDistanceLessThanOne(self, x, y):
        return math.pow(x, 2) + math.pow(y, 2) <= 1

    """
        This function is used to get a uniform random number between 0 and 1
    """
    def getUniformRandomNumberBetweenLimits(self):
        return np.random.uniform(0.0, 1.0)

    """
        This function is used to calculate the value of Pi
        and find the iteration at which the calculate value
        of Pi is close to the actual value
    """
    def calculatePiN(self):
        index = 0
        count = 0
        i = 0
        while index < len(self.boundaries):
            x, y = self.getUniformRandomNumberBetweenLimits(), self.getUniformRandomNumberBetweenLimits()

            if self.isDistanceLessThanOne(x, y):
                count += 1
            # calculating the value of pi, by multiplying (pi/4) * 4
            piN = (count * 4)/(i+1)
            if abs(piN - math.pi) < self.boundaries[index]:
                print("Boundary condition |PiN -Pi| < {} reached".format(self.boundaries[index]))
                print("Pi N: {} at iteration {}".format(piN, i+1))
                print("Diff. between calculated Pi and actual Pi: {}\n".format(abs(piN - math.pi)))
                index += 1

            i += 1

if __name__ == "__main__":
    uno = questionUno()
    uno.calculatePiN()