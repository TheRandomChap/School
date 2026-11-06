import math 
from math import *
import numpy as np
import matplotlib.pyplot as plt

#def test():



def tegn_graf(function, x_min=-10, x_max=10):
    x_values = np.linspace(x_min, x_max, 400)
    y_values = function(x_values)

    plt.plot(x_values, y_values)
    plt.title("Graf")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()


# Example: f(x) = x²
tegn_graf(lambda x: 2*x*2+10)