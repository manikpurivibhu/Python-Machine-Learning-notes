class Network:
    def __init__(self):
        self.layers = []
        self.cost   = None
        self.cost_derivative = None

    def add(self, layer):
        '''add layer to network (Dense/ActivationLayer)'''
        self.layers.append(layer)

    def use(self, cost, cost_derivative):
        '''set Cost function and it's derivative to use'''
        self.cost = cost
        self.cost_derivative = cost_derivative

    def predict(self, input_data):
        '''predict output for given input'''
        
        #sample dimension first
        samples = len(input_data)
        result  = []

        #run network over all samples
        for i in range(samples):
            #forward propagation
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)
        print(type(result))
        return result

    def fit(self, x_train, y_train, epochs, learning_rate):
        '''train the Neural Network'''

        #epoch means one complete pass of the training dataset through the algorithm
        #i.e. the number of times a learning algorithm sees the complete dataset.
        
        #sample dimension first
        samples = len(x_train)

        #training loop
        for e in range(epochs):
            err = 0
            for x, y in zip(x_train, y_train):
                #forward propagation
                output = x
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                #compute cost (for display purpose only)
                err += self.cost(y, output)

                #backpropagation
                grad = self.cost_derivative(y, output)
                for layer in reversed(self.layers):
                    grad = layer.backward_propagation(grad, learning_rate)

            #calculate average error on all samples
            err /= samples
            print('epoch %d/%d   error=%f' % (e+1, epochs, err))
