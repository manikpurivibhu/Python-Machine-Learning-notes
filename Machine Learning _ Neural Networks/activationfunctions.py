import numpy as np

# activation function and its derivative
def activation_function(x):
    return np.tanh(x)

def activation_function_derivative(x):
    return 1-np.tanh(x)**2