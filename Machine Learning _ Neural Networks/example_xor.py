import numpy as np

from network import Network
from denselayer import DenseLayer
from activationlayer import ActivationLayer
from activationfunctions import activation_function, activation_function_derivative
from losses import cost_fun, cost_derivative

# training data
x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
y_train = np.array([[[0]], [[1]], [[1]], [[0]]])

# network
net = Network()
  
net.add(DenseLayer(2, 3))
net.add(ActivationLayer(activation_function, activation_function_derivative))
net.add(DenseLayer(3, 1))
net.add(ActivationLayer(activation_function, activation_function_derivative))
print('Network Architecure established! \n')

# train
net.use(cost_fun, cost_derivative)
net.fit(x_train, y_train, epochs=1000, learning_rate=0.1)
print('Neural Network trained! \n')

# test
output = net.predict(x_train)

result = []
for no in output:
    if no[0,0] <0.5:
        result.append(0)
    else:
        result.append(1)

print(output)
print('Output:\n',result)