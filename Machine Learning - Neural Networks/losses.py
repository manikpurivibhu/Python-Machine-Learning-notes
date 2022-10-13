import numpy as np

#Cost function and its derivative
def cost_fun(y_true, y_pred):
    '''
    define Cost Function
    '''
    return np.mean(np.power(y_true-y_pred, 2))

def cost_derivative(y_true, y_pred):
    '''
    define derivative of the Cost Function
    '''
    return 2*(y_pred-y_true)/y_true.size