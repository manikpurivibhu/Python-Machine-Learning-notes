from layer import Layer
import numpy as np

#inherit from base class Layer
class DenseLayer(Layer):
    #input_size = number of input neurons
    #output_size = number of output neurons

    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias    = np.random.rand(1, output_size) - 0.5

    #returns output for a given input
    def forward_propagation(self, input_data):
        self.input  = input_data
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output

    #computes dE/dW, dE/dB for a given output_error(output_gradient)=dE/dY. Returns input_error(input_gradient)=dE/dX.
    def backward_propagation(self, output_gradient, learning_rate):
        input_gradient   = np.dot(output_gradient, self.weights.T)
        weights_gradient = np.dot(self.input.T, output_gradient)

        #update parameters
        self.weights -= learning_rate * weights_gradient
        self.bias    -= learning_rate * output_gradient
        return input_gradient